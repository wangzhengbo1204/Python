#-*- coding:utf-8 -*-
'''
Created on 2012-4-20

@author: GFTOwenWang
'''
import sys
import time
import atexit

def goodbye(name, adjective):
    print 'Goodbye, %s, it was %s to meet you.' % (name, adjective)
atexit.register(goodbye, 'Donny', 'nice')


@atexit.register
def myexit():
    print 'call myexit'
    sys.exit(1)


def func1():
    print 'hello.'
    time.sleep(10)

def func2():
    a=1/0
    print a
    
def func3():
    try:
        a=1/0
        print a
    except Exception as ex:
        print ex
        
def func4():
    print __file__
    
    
        
    
if __name__ == '__main__':
    func4()