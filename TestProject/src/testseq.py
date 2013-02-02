#-*- coding:utf-8 -*-
'''
Created on 2012-7-26

@author: GFTOwenWang
'''


def func1():
    a=(1,2,3,4)
    a = a[:2]
    print a
    b = func2(a)
    print b
    print a
    
def func2(tuple_id):
    tuple_id=tuple_id + (9,1)
    return tuple_id


if __name__ == "__main__":
    func1()