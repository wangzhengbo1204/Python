#-*- coding:utf-8 -*-
'''
Created on 2013-3-6

@author: GFTOwenWang
'''
import clr
clr.AddReference("ClassLibrary1")

from ClassLibrary1 import Class1

c = Class1()
r  = c.add(1,2)
print r