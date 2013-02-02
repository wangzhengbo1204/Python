#-*- coding:utf-8 -*-
'''
Created on 2012-10-11

@author: GFTOwenWang
'''
import MySQLdb
import pygrametl

from datetime import datetime, date

from pygrametl.datasources import CSVSource,MergeJoiningSource
from pygrametl.tables import CachedDimension


def func1():
    pgconn = MySQLdb.Connect(host="192.168.1.42",port=3307, user="datatec",passwd="0.618", db="test",charset="utf8")
    connection = pygrametl.ConnectionWrapper(pgconn)
    connection.setasdefault()

    student = CSVSource(file("./resource/student.txt",'r',100000),delimiter=',')

    studentdim=CachedDimension(name="Student",
                              key="id",
                              attributes=("studentid",'name',"birthday"),
                              lookupatts=("studentid",))
    
    score = CSVSource(file("./resource/studentscore.txt",'r',100000),delimiter=',')

    scoredim=CachedDimension(name="StudentScore",
                              key="id",
                              attributes=("studentid",'coursename',"score"),
                              lookupatts=("studentid",))
    
    mjdata = MergeJoiningSource(student,'no',score,'no')
    
    for row in mjdata:
        row['birthday'] =  datetime.strptime(row['birthday'],'%Y-%m-%d').date()#pygrametl.getdate(connection,row['birthday']) # Convert to an date
        studentdim.ensure(row, {'studentid':'no'})
        scoredim.ensure(row, {'studentid':'no','coursename':'course'})
        
    connection.commit()
        

if __name__ == "__main__":
    func1()