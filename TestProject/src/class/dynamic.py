'''
Created on 2012-4-16

@author: GFTOwenWang
'''


class A(object):
    
    def call(self):
        pass
    
class B(A):
    
    def call(self):
        print "Call of B"
        
        
class C(A):
    
    def call(self):
        print "Call of C"