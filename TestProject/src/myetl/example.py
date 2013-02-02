
# This is code for loading the DW from the running example 
# presented in C. Thomsen & T.B. Pedersen: "pygrametl: A Powerful Programming 
# Framework for Extract--Transform--Load Programmers"
#
# It is made to be used with PostgreSQL and psycopg2 but you can
# modify it to work with another DBMS.


#  
#  Copyright (c) 2009, 2010 Christian Thomsen ( chr @ cs . aau . dk )
#  
#  This file is free software: you may copy, redistribute and/or modify it  
#  under the terms of the GNU General Public License version 2 
#  as published by the Free Software Foundation.
#  
#  This file is distributed in the hope that it will be useful, but  
#  WITHOUT ANY WARRANTY; without even the implied warranty of  
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU  
#  General Public License for more details.  
#  
#  You should have received a copy of the GNU General Public License  
#  along with this program.  If not, see http://www.gnu.org/licenses.  
#  


import datetime
import sys
import time

# In this example, we use psycopg2. You can change it to another driver,
# but then the method pgcopybulkloader won't work as we use driver-specific
# code there. 
# You can make another function or declare facttbl (see further below) to 
# be a BatchFactTable such that you don't need special 
# bulk loading methods.

#import psycopg2
import MySQLdb

# Depending on your system, you might have to do something like this
# where you append the path where pygrametl is installed
sys.path.append('/home/me/code') 

import pygrametl
from pygrametl.datasources import CSVSource, MergeJoiningSource
from pygrametl.tables import CachedDimension, SnowflakedDimension,\
    SlowlyChangingDimension, BulkFactTable


# Connection to target DW:
#pgconn = psycopg2.connect(user='me')
pgconn = MySQLdb.Connect(host="192.168.1.42",port=3307, user="datatec",passwd="0.618", db="test",charset="utf8")
connection = pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
#connection.execute('set search_path to pygrametlexa')


# Methods
def pgcopybulkloader(name, atts, fieldsep, rowsep, nullval, filehandle):
    # Here we use driver-specific code to get fast bulk loading.
    # You can change this method if you use another driver or you can
    # use the FactTable or BatchFactTable classes (which don't require
    # use of driver-specifc code) instead of the BulkFactTable class.
    global connection
    curs = connection.cursor()
    curs.copy_from(file=filehandle, table=name, sep=fieldsep,
                   null=str(nullval), columns=atts)

def datehandling(row, namemapping):
    # This method is called from ensure(row) when the lookup of a date fails.
    # In the Real World, you would probably prefill the date dimension, but
    # we use this to illustrate "rowexpanders" that make it possible to
    # calculate derived attributes on demand (such that the - possibly
    # expensive - calculations only are done when needed and not for each
    # seen data row).
    #
    # Here, we calculate all date related fields and add them to the row.
    date = pygrametl.getvalue(row, 'date', namemapping)
    (year, month, day, hour, minute, second, weekday, dayinyear, dst) = \
        time.strptime(date, "%Y-%m-%d")
    (isoyear, isoweek, isoweekday) = \
        datetime.date(year, month, day).isocalendar()
    row['day'] = day
    row['month'] = month
    row['year'] = year
    row['week'] = isoweek
    row['weekyear'] = isoyear
    row['dateid'] = dayinyear + 366 * (year - 1990) #Support dates from 1990
    return row
    

def extractdomaininfo(row):
    # Take the 'www.domain.org' part from 'http://www.domain.org/page.html'
    # We also the host name ('www') in the domain in this example.
    domaininfo = row['url'].split('/')[-2]
    row['domain'] = domaininfo
    # Take the top level which is the last part of the domain
    row['topleveldomain'] = domaininfo.split('.')[-1]

def extractserverinfo(row):
    # Find the server name from a string like "ServerName/Version"
    row['server'] = row['serverversion'].split('/')[0]

# Dimension and fact table objects
topleveldim = CachedDimension(
    name='topleveldomain', 
    key='topleveldomainid',
    attributes=['topleveldomain'])

domaindim = CachedDimension(
    name='domain', 
    key='domainid', 
    attributes=['domain', 'topleveldomainid'],
    lookupatts=['domain'])

serverdim = CachedDimension(
    name='server', 
    key='serverid',
    attributes=['server'])

serverversiondim = CachedDimension(
    name='serverversion', 
    key='serverversionid',
    attributes=['serverversion', 'serverid'])

pagedim = SlowlyChangingDimension(
    name='page', 
    key='pageid',
    attributes=['url', 'size', 'validfrom', 'validto', 'version', 
                'domainid', 'serverversionid'],
    lookupatts=['url'],
    versionatt='version', 
    fromatt='validfrom',
    toatt='validto', 
    srcdateatt='lastmoddate',
    cachesize=-1)

pagesf = SnowflakedDimension(
    [(pagedim, (serverversiondim, domaindim)),
     (serverversiondim, serverdim),
     (domaindim, topleveldim)
     ])

testdim = CachedDimension(
    name='test', 
    key='testid',
    attributes=['testname', 'testauthor'],
    lookupatts=['testname'], 
    prefill=True, 
    defaultidvalue=-1)

datedim = CachedDimension(
    name='date', 
    key='dateid',
    attributes=['date', 'day', 'month', 'year', 'week', 'weekyear'],
    lookupatts=['date'], 
    rowexpander=datehandling)

facttbl = BulkFactTable(
    name='testresults', 
    keyrefs=['pageid', 'testid', 'dateid'],
    measures=['errors'], 
    bulkloader=pgcopybulkloader,
    bulksize=5000000)


# Data sources - change the path if you have your files somewhere else
downloadlog = CSVSource(file('./a.csv', 'r', 16384),
                        delimiter='\t')

testresults = CSVSource(file('./b.csv', 'r', 16384),
                        delimiter='\t')

inputdata = MergeJoiningSource(downloadlog, 'localfile', 
                               testresults, 'localfile')

def main():
    for row in inputdata:
        extractdomaininfo(row)
        extractserverinfo(row)
        row['size'] = pygrametl.getint(row['size']) # Convert to an int
        # Add the data to the dimension tables and the fact table
        row['pageid'] = pagesf.scdensure(row)
        row['dateid'] = datedim.ensure(row, {'date':'downloaddate'})
        row['testid'] = testdim.lookup(row, {'testname':'test'})
        facttbl.insert(row)
    connection.commit()

if __name__ == '__main__':
    main()

