#-*- coding:utf-8 -*-
'''
Created on 2012-3-22

@author: GFTOwenWang
'''
import httplib, urllib


def func1():
    url = r"180.96.8.44"
    conn = httplib.HTTPConnection(url)
    headers = {"wind.sessionid":"8a9be2475a2049e9ad35cc168fc8bb59"}
    r = conn.request("GET", "/speedweb/swintf.aspx?f=w&bp=1&a1=2,8,6,5,7,11,12,115,116,114,119,120,121,118,123,124,27,28,29,103,38,39,30,&rd=7", {}, headers)
    f = conn.getresponse()
    print f.status, f.reason
    print "done"
    
def func2():
    url = r"http://epp.eurostat.ec.europa.eu/tgm/table.do?tab=table&init=1&language=en&pcode=teicp000"
    r = urllib.urlopen(url)
    print r.read()
    
def func3():
    url = r"www.baidu.com"
    conn = httplib.HTTPConnection(url)
    r = conn.request("GET", url, {}, {})
    f = conn.getresponse()
    print f.status, f.reason
    print "done"
    
if __name__ == "__main__":
    func1()