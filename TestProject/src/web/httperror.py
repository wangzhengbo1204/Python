#-*- coding:utf-8 -*-
'''
Created on 2012-6-7

@author: GFTOwenWang
'''
import urllib2


def func1():
    url ="http://www.microbell.com/docdetail_719254.html"
    r = urllib2.urlopen(url)
    print r.read()
    
    
if __name__ == '__main__':
    func1()
    