#-*- coding:utf-8 -*-
'''
Created on 2012-12-5 @author: GFTOwenWang
'''


d1 = {'a':'abc ','b':' efg'}

d1 = dict((k,unicode(v).strip()) for k,v in d1.iteritems())

print d1