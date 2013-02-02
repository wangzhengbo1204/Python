#-*- coding:utf-8 -*-
'''
Created on 2012-11-22 @author: GFTOwenWang
'''
import cProfile
import profile
import pstats


def func1():
    for i in range(1000):
        r = func2(i)
        #print r 
    
def func2(n):
    return n**2


if __name__ == "__main__":
    cProfile.run("func1()")
    