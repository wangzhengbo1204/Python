'''
Created on 2012-2-20

@author: GFTOwenWang
'''

class Singleton(type):
    
    def __init__(cls, name, base, dict):
        super(Singleton, cls).__init__(name, base, dict)
        cls.instance = None
        
        
    def __call__(cls, *args, **kw): #@NoSelf
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        
        return cls.instance
    
    
    

class MyClass(object):
    __metaclass__ = Singleton
    
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        
    def hello(self):
        print "hello, %s, %s" %(self.name, self.age)
    


b= MyClass('vim', 22)
b.hello()

a = MyClass('owen', 23)
a.hello()

print dir(a)