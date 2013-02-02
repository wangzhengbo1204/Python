'''
Created on 2012-3-6

@author: GFTOwenWang
'''

class Singleton(object):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        
        return cls._instance
    

class A(Singleton):
    
    def __init__(self):
        self.init()
    
    def init(self):
        self.name = "owen"
        self.age = 1
        
class B(A):
    
    def __init__(self):
        A.__init__(self)
        self.init2()
    
    def init2(self):
        self.corp="gft"
        

def func1():
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print "same"
    else:
        print "different"
        
def func2():
    s1=Singleton("owen", 1)
    s2 = Singleton("vie",2)
    print s1.name,s1.age
    print s2.name, s2.age
        
def func3():
    a1= A()
    a2= A()
    print a1 is a2
    print a1.name, a1.age
    print a2.name, a2.age
    
def func4():
    b1 = B()
    b2 = B()
    print b1 is b2
    print b1.name , b1.age
    
        
if __name__ == "__main__":
    func4()