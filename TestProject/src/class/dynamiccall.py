'''
Created on 2012-4-16

@author: GFTOwenWang
'''
import dynamic


def func1():
    b=getattr(dynamic, 'B')
    b1 = b()
    b1.call()
    
    c=getattr(dynamic, 'C')
    c1 = c()
    c1.call()
    
    d=getattr(dynamic, 'D')
    d1 = d()
    d1.call()
    
    
if __name__=='__main__':
    func1()