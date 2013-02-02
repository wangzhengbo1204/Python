'''
Created on 2012-10-22

@author: GFTOwenWang
'''


class A(object):
    
    _instance=None
    def __init__(self,name,age):
        '''
        
        @param name:
        @param age:
        '''
        if A._instance:
            pass
            #self = A._instance
        else: 
            self.name = name
            self.age = age
            self.birthday()
            A._instance = self
        
    def birthday(self):
        self.birth='2012-8-1'
        
def test_A():
    a1=A('owne',1)
    print a1.name, a1.age, a1.birth
    
    a2=A('corleone',2)
    print type(a2) 
    print a2.name, a2.age, a2.birth
    
if __name__ == "__main__":
    test_A()