'''
Created on 2011-9-8

@author: GFTOwenWang
'''

class TestClass(object):
    
    masterdb = None
    appdb = None
    logdb = None
    
    def __init__(self, master, app, log):
        TestClass.masterdb = master
        TestClass.appdb = app
        TestClass.logdb = log
        

c1 = TestClass(1,2,3)

print c1.masterdb

c2 = TestClass(4,5,6)

print c1.masterdb
print c2.masterdb


class TestClass2(object):
    
    masterdb = None
    appdb = None
    logdb = None
    
    def __init__(self, master, app, log):
        self.masterdb = master
        self.appdb = app
        self.logdb = log
        

c1 = TestClass2(1,2,3)

print c1.masterdb

c2 = TestClass2(4,5,6)

print c1.masterdb
print c2.masterdb


class A(object):
    
    def __init__(self, a, b):
        self._a = a
        self._b = b
        
class B(A):
    
    def __init__(self, a, b, c):
        super(B, self).__init__(a,b)
        self._c = c
        
        
print '='*20
ca= A(1,2)
cb=B(1,2,3)
print dir(cb)
