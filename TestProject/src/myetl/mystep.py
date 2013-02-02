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
from pygrametl.steps import Step


class AddStep(Step):
    
    def process(self, row):
        self.__redirected = True
        self.__row = row
        self.worker(row)
        self.__row = None
        if self.next is None or self.__redirected:
            if row['a']>103:
                #self.next='step_c'
                self._inject(row, "step_c")
            else:
                #self.next='step_b'
                self._inject(row, "step_b")
        else:
            self._inject(row, self.next)
        
    def _inject(self, row, target):
        Step._inject(self,{'e':5} , target)
        Step._inject(self, row, target)
#        if target is None:
#            target = self.next
#
#        if isinstance(target, Step):
#            target.process({'e':5})
#            target.process(row)
#        else:
#            #self.__class__.__steps[target].process({'e':5})
#            #self.__class__.__steps[target].process(row)
#            pass

def step1():
    def func1(row):
        for key,value in row.items():
            row[key]=value+100
            
        return row
    
    def func2(row):
        print row
        
    def func3(row):
        print "this is:", row
            
    step_3=Step(worker=func3,next=None,name='step_c')
    step_2=Step(worker=func2,next=None,name='step_b')
    step_1=AddStep(worker=func1,next='step_b',name='step_a')
    
    list_row=[{'a':1,'b':1,'c':1},{'a':2,'b':2,'c':2},{'a':3,'b':3,'c':3},{'a':4,'b':4,'c':4},{'a':5,'b':5,'c':5},]
    for row in list_row:
        step_1.process(row)
    
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
    #func1()
    step1()