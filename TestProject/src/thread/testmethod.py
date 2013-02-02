#-*- coding:utf-8 -*-
'''
Created on 2012-3-16

@author: GFTOwenWang
'''
import threading
import time

def func1():
    print "func1 sleep 10 seconds"
    time.sleep(10)
    
def func2():
    print "func2 sleep 5 seconds"
    time.sleep(5)
    
def main():
    print 'biegin...'
    thread1 = threading.Thread(target=func1, args=(), name='f1')
    thread1.start()
    
    thread2 = threading.Thread(target=func2, args=(), name='f2')
    thread2.start()
    
    t = threading.currentThread()
    print t.name
    time.sleep(3)
    num = threading.active_count()
    print num
    
    threading.Thread.join(thread1)
    
    threading.Thread.join(thread2)
    
    print "end"
    
    
if __name__ == '__main__':
    main()