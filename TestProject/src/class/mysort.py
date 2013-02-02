'''
Created on 2012-4-17

@author: GFTOwenWang
'''
import copy
from datetime import datetime


class A(object):
    
    def __init__(self, name, birthday, num=None):
        self.name = name
        self.birthday = birthday
        self.num=num
        
    def __lt__(self, other):
        r = cmp(self.birthday,other.birthday)
        #return True if r < 0 else False
        return True
        
    def __str__(self):
        return u"Name:%s; Birthday:%s" % (self.name, self.birthday)
        
        
def func1():
#    a1 = A('a1',datetime.strptime("2011-12-1", "%Y-%m-%d"))
#    a2 = A('a2',datetime.strptime("2012-5-2", "%Y-%m-%d"))
#    a3 = A('a3',datetime.strptime("2012-5-2", "%Y-%m-%d"))
#    a4 = A('a4',datetime.strptime("2012-3-10", "%Y-%m-%d"))
#    a5 = A('a5',datetime.strptime("2011-10-3", "%Y-%m-%d"))    
    
    a1 = A('a1',datetime.strptime("2012-12-1", "%Y-%m-%d"))
    a2 = A('a2',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a3 = A('a3',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a4 = A('a4',datetime.strptime("2012-3-10", "%Y-%m-%d"))
    a5 = A('a5',datetime.strptime("2011-10-3", "%Y-%m-%d"))   
    
    list_a = [a1,a2,a3,a4,a5]
    list_a = sorted(list_a,key=lambda x: (x.birthday))  
    
    for a in list_a:
        print a
        
def mycmp(a1, a2):
    print a1
    print a2
    r = cmp(a2.birthday,a1.birthday)
    return True if r < 0 else False
    #return True

def mycmp2(a1, a2):
    print a1
    print a2
    if a1[1].birthday == a2[1].birthday:
        return cmp(a1[0],a2[0])
    else:
        return cmp(a2[1].birthday,a1[1].birthday)

def func2():
    a1 = A('a1',datetime.strptime("2012-12-1", "%Y-%m-%d"))
    a2 = A('a2',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a3 = A('a3',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a4 = A('a4',datetime.strptime("2012-3-10", "%Y-%m-%d"))
    a5 = A('a5',datetime.strptime("2011-10-3", "%Y-%m-%d"))   
    
    list_a = [a1,a2,a3,a4,a5]
    
    list_a2=[]
    for a in enumerate(list_a):
        for b in enumerate(list_a):
            if a<b:
                a=copy.deepcopy(b)
                k=j+index+1
        list_a2.append(a)
        
    for a in list_a2:
        print a
        
def func3():
    a1 = A('a1',datetime.strptime("2012-12-1", "%Y-%m-%d"))
    a2 = A('a2',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a3 = A('a3',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a4 = A('a4',datetime.strptime("2012-3-10", "%Y-%m-%d"))
    a5 = A('a5',datetime.strptime("2011-10-3", "%Y-%m-%d"))  
    a6 = A('a6',datetime.strptime("2012-10-3", "%Y-%m-%d"))   
    
    list_a = [a1,a2,a3,a4,a5,a6]
    
    list_a2=sorted(list_a, mycmp,None, True)
        
    for a in list_a2:
        print a
        
    print '-'*20
    for a in list_a2:
        print a
                
def func4():
    a1 = A('a1',datetime.strptime("2012-12-1", "%Y-%m-%d"))
    a2 = A('a2',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a3 = A('a3',datetime.strptime("2012-5-2", "%Y-%m-%d"))
    a4 = A('a4',datetime.strptime("2012-3-10", "%Y-%m-%d"))
    a5 = A('a5',datetime.strptime("2011-10-3", "%Y-%m-%d"))  
    a6 = A('a6',datetime.strptime("2012-10-3", "%Y-%m-%d"))   
    
    list_a = [a1,a2,a3,a4,a5,a6]
    
    a = [i[1] for i in sorted([(idx,x) for idx,x in enumerate(list_a)],cmp=mycmp2)]
    
    for i in a:
        print i
    

    for i in [(idx,x) for idx,x in enumerate(list_a)]:
        print unicode(i[0]),str(i[1])
                
                
def mycmp3(a1, a2):
    if a1.birthday == a2.birthday:
        return cmp(a1.num, a2.num)
    else:
        return cmp(a1.birthday, a2.birthday)
    
def func5():
    a1 = A('a1',datetime.strptime("2012-12-1", "%Y-%m-%d"),1)
    a2 = A('a2',datetime.strptime("2012-5-2", "%Y-%m-%d"),3)
    a3 = A('a3',datetime.strptime("2012-5-2", "%Y-%m-%d"),2)
    a4 = A('a4',datetime.strptime("2012-3-10", "%Y-%m-%d"),4)
    a5 = A('a5',datetime.strptime("2011-10-3", "%Y-%m-%d"),5)  
    a6 = A('a6',datetime.strptime("2012-10-3", "%Y-%m-%d"),6)   
    
    list_a = [a1,a2,a3,a4,a5,a6]
    
    list_a2= sorted(list_a, cmp=mycmp3)
    
    for a in list_a2:
        print a
    
        
if __name__ == '__main__':
    func5()
    
    
