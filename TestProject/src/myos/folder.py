#-*- coding:utf-8 -*-
'''
Created on 2012-8-22

@author: GFTOwenWang
'''
import os
import shutil

def test_func1():
    path = u"//172.16.101.115/upload"
    files = os.listdir(path)
    print files
    
    shutil.copy(ur"d:\a.txt", path)
    print 'done'
    

if __name__=="__main__":
    test_func1()

