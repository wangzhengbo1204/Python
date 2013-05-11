#-*-coding:utf-8 -*-
'''
Created on 2013-3-2

@author: Administrator
'''

import lxml
import urllib2


def readhtml():
    url = ""
    
def analyst():
    me_set = set(['02','04','05','08','12','27'])
    me_set = set(['04','08','12','10','25','27','10'])
    f = open(r"f:\doublecolor.TXT",'rb')
    count = 0
    for line in f.readlines():
        fields = line.split(" ")
        p_set = set(fields[1:7])
        #print fields[0], p_set
        cross_set = me_set & p_set
        if len(cross_set) >3:
            print line
            count += 1
            
    print count
        
        
def test():
    s1 = set([2,3,4])
    s2 = set([3,5,6])    
    s3 = s1 & s2
    print s3
    print len(s3)
    
if __name__ == '__main__':
    analyst()
    #test()
    