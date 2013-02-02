'''
Created on 2012-3-20

@author: GFTOwenWang
'''

class A(object):
    x=None
    y=None
    
    def __init__(self):
        pass
    
    def setx(self, value):
        self.x = value
        
    
print dir(A)
print type(A.__dict__)
print A.__dict__
#A.__dict__['z']=1

a1 = A()
A.__setattr__('z', 1)


print a1.z
A.z = A.z + 1

a2 = A()
print a2.z