#-*- coding:utf-8 -*-
'''
Created on 2012-10-18

@author: GFTOwenWang
'''

def func1():
    a=[('b',2),('a',1),('c',3)]
    print a
    b=sorted(a,cmp=lambda x,y:cmp(x[1],y[1]))
    print b
    

if __name__ == "__main__":
    func1()