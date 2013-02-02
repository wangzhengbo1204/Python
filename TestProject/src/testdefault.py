# -*- coding:utf-8 -*-
'''
Created on 2011-9-11

@author: GFTOwenWang
'''


def test1(name, list_names=[]):
    list_names.append(name)
    
    return list_names


if __name__ == '__main__':
    list_a = test1('a')
    print list_a
    
    list_a = test1('b')
    print list_a
    
    list_b = test1(1)
    print list_b
    
    list_b = test1(2)
    print list_b