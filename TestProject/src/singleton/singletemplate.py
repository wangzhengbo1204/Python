#-*- coding:utf-8 -*-
'''
Created on 2012-3-6

@author: GFTOwenWang
'''
import threading


class Singleton(object):
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls,*args, **kwargs):
        cls._lock.acquire()
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        cls._lock.release()
            
        return cls._instance
    
    def __init__(self):
        pass
    
    
class SingletonParam(object):
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, a, b,*args, **kwargs):
        cls._lock.acquire()
        if cls._instance is None:
            cls._instance = super(SingletonParam, cls).__new__(cls, *args, **kwargs)
        cls._lock.release()
            
        return cls._instance
    
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

s1 = Singleton()
s2=Singleton()
print s1 is s2

s3 = SingletonParam("owen", 1)
s4=SingletonParam("vie", 2)

print s3 is s4
print s3.name , s4.age
