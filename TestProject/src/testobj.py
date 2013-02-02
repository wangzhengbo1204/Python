'''
Created on 2011-8-13

@author: GFTOwenWang
'''

class TestObj(object):
    
    def __init__(self, a=[], b=None):
        self._a = a
        self._b = b
        
    def init(self, a, b):
        self._a = a
        self._b = b
        

list_testObj = []
for i in range(10):
    testObj = TestObj()
    testObj.init([i, i], i)
    list_testObj.append(testObj)
    
    
for testObj in list_testObj:
    print testObj._a, testObj._b


