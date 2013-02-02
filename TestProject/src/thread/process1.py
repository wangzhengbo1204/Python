'''
Created on 2012-3-31

@author: GFTOwenWang
'''
from multiprocessing import Process, Pipe, Queue
import os
import time


def info(title):
    print title
    print 'module name:', __name__
    #print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name
    
def f2(q):
    q.put([42, None, 'hello'])
    q.put([1, 2, 'abc'])
    

if __name__ == '__main__':
#    info('main line')
#    p = Process(target=f, args=('bob',))
#    p.start()
#    p.join()
    q = Queue()
    p = Process(target=f2, args=(q,))
    p.start()
    time.sleep(2)
    print q.qsize()
    print q.get()    # prints "[42, None, 'hello']"
    p.join()


