
#  Copyright (c) 2011 Christian Thomsen (chr@cs.aau.dk)
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
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.  
#  


import datetime
import sys
import time

# Depending on your system you might have to do something like this
# where you append the path where pygrametl is installed
sys.path.append('/home/chr/code/') 

import pygrametl
from pygrametl.JDBCConnectionWrapper import JDBCConnectionWrapper
from pygrametl.datasources import CSVSource, MergeJoiningSource, ProcessSource,\
    TransformingSource
from pygrametl.tables import CachedDimension, SnowflakedDimension,\
    SlowlyChangingDimension, BulkFactTable, FactTable, \
    DecoupledDimension, DecoupledFactTable, DimensionPartitioner
from pygrametl.parallel import shareconnectionwrapper,\
     getsharedsequencefactory

import java.lang


BATCHSIZE = 500


def pgbulkloader(name, atts, fieldsep, rowsep, nullval, filename):
    filehandle = open(filename, 'r')
    sql = "COPY %s(%s) FROM STDIN WITH DELIMITER '%s'" %\
          (name, ', '.join(atts), fieldsep)
    global rawconn
    copymgr = rawconn.getCopyAPI()
    copymgr.copyIn(sql, filehandle)

# Connection to target DW:
java.lang.Class.forName("org.postgresql.Driver")
rawconn = java.sql.DriverManager.getConnection \
           ("jdbc:postgresql://localhost/chr?user=chr")
shrdconn = shareconnectionwrapper(JDBCConnectionWrapper(rawconn), 10,
                                   (pgbulkloader,))
shrdconn.execute('set search_path to pygrametlexa')



def datehandling(row, namemapping):
    # This method is called from ensure(row) when the lookup of a date fails.
    # We have to calculate all date related fields and add them to the row.
    date = pygrametl.getvalue(row, 'date', namemapping)
    (year, month, day, hour, minute, second, weekday, dayinyear, dst) = \
        time.strptime(date, "%Y-%m-%d")
    (isoyear, isoweek, isoweekday) = \
        datetime.date(year, month, day).isocalendar()
    # We could use row[namemapping.get('day') or 'day'] = X to support name map.
    row['day'] = day
    row['month'] = month
    row['year'] = year
    row['week'] = isoweek
    row['weekyear'] = isoyear
    row['dateid'] = dayinyear + 366 * (year - 1990) #Allow dates from 1990-01-01
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


def convertsize(row):
    row['size'] = pygrametl.getint(row['size'])

# Dimension and fact table objects

def getpagediminstances():
    global shrdconn
    idfactory = getsharedsequencefactory(0)
    for i in range(2):
        yield DecoupledDimension(
            SlowlyChangingDimension(
            name='page', 
            key='pageid',
            attributes=['url', 'size', 'domain', 'topleveldomain', 
                        'serverversion', 'server', 
                        'validfrom', 'validto', 'version'],
            lookupatts=['url'],
            versionatt='version', 
            fromatt='validfrom',
            toatt='validto', 
            srcdateatt='lastmoddate', 
            cachesize=-1,
            prefill=True,
            idfinder=idfactory(),
            targetconnection=shrdconn.copy()),
            batchsize=BATCHSIZE, queuelength=10
            )

pagedim = DimensionPartitioner([pd for pd in getpagediminstances()])

testdim = CachedDimension(
    name='test', 
    key='testid',
    attributes=['testname', 'testauthor'],
    lookupatts=['testname'], 
    prefill=True,
    defaultidvalue=-1,
    targetconnection=shrdconn.copy())

datedim = CachedDimension(
    name='date', 
    key='dateid',
    attributes=['date', 'day', 'month', 'year', 'week', 'weekyear'],
    lookupatts=['date'], 
    rowexpander=datehandling,
    prefill=True,
    targetconnection=shrdconn.copy())

facttbl = DecoupledFactTable(
    BulkFactTable(
        name='testresults', 
        keyrefs=['pageid', 'testid', 'dateid'],
        measures=['errors'], 
        bulksize=250000,
        bulkloader=shrdconn.copy().pgbulkloader,
        usefilename=True),
    batchsize=BATCHSIZE, queuelength=10,
    consumes=pagedim.parts,
    returnvalues=False
    )


# Data sources - change the path if you have your files somewhere else
downloadlog = CSVSource(file('DownloadLog.csv', 'r'),
                        delimiter='\t')
    

testresults = CSVSource(file('TestResults.csv', 'r'),
                        delimiter='\t')


joineddata = MergeJoiningSource(downloadlog, 'localfile', testresults,
                                'localfile')

transformeddata = TransformingSource(joineddata, extractdomaininfo, 
                                     extractserverinfo, convertsize)


inputdata = ProcessSource(transformeddata, batchsize=BATCHSIZE, queuesize=10)

def main():
    for row in inputdata:
        fact = {'errors':row['errors']}
        fact['pageid'] = pagedim.scdensure(row)
        fact['dateid'] = datedim.ensure(row, {'date':'downloaddate'})
        fact['testid'] = testdim.lookup(row, {'testname':'test'})
        facttbl.insert(fact)
    shrdconn.commit()

if __name__ == '__main__':
    main()
