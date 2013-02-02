#-*- coding:utf-8 -*-
'''
Created on 2011-8-8

@author: GFTOwenWang
'''
import hashlib


def test_hash():
    f1 = ur'd:\国债.xls'
    f2 = ur'd:\国债2.xls'
    #f1 = ur'd:\test2_2_2.txt'
    #f2 = ur'd:\test2_2.txt'
    f1=ur'd:\FL0000051W.pdf'
    file1 = open(f1, 'rb')
    file2 = open(f2, 'rb')
    
    m1= hashlib.md5()
    m1.update(file1.read())
    a1= m1.hexdigest()
    print a1
    
    m2 = hashlib.md5()
    m2.update(file2.read())
    a2=m2.hexdigest()
    print a2
    
def test_sha224():
    f1 = ur'd:\test2_2_2.txt'
    f2 = ur'd:\test2_2.txt'
    file1 = open(f1, 'rb')
    file2 = open(f2, 'rb')
    
    m1= hashlib.sha224(file1.read())
    print m1.hexdigest()
    
    m2= hashlib.sha224(file2.read())
    print m2.hexdigest()
    

if __name__ == '__main__':
    test_hash()
    #test_sha224()
    
    