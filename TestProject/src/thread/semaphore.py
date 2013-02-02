'''
Created on 2012-3-28

@author: GFTOwenWang
'''
import threading

bs = threading.BoundedSemaphore(value=5)

def func1():
    print 'begin'
    for i in range(30):
        t = threading.Thread(target=func3, args=(i,))
        t.start()
        
    print 'end'
    
    
def func2(num):
    bs.acquire(blocking=0)
    i = 0
    while i<10000:
        i = i + 1
        
    print 'func2(%s) is called, num:%s' % (num,threading.activeCount())
    
    bs.release()
    
def func3(num):
    with bs:
        i = 0
        while i<10000:
            i = i + 1
            
        print 'func2(%s) is called, num:%s' % (num,threading.activeCount())

    
if __name__ == '__main__':
    func1()
    