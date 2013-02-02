#-*- coding:utf-8 -*-
'''
Created on 2012-3-20

@author: GFTOwenWang
'''
import socket
import urllib2
import chardet
import gzip
import StringIO

def func1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('72.246.25.10',80))
    
#def func2():
#    proxy_support = urllib2.ProxyHandler({'http':'72.241.25.99:80'})
#    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
#    try:
#        url = u"http://www.sina.com"
#        r = urllib2.urlopen(url)    
#        r2 = r.read()
#        print r2
#        print "="*40
#        print r2.decode("gbk")
#    except IOError, e:
#        print e

def func2():
    proxy_support = urllib2.ProxyHandler({'http':'212.156.150.130:8080'})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    #urllib2.install_opener(opener)
    try:
        url = u"http://www.sina.com"
        #r = urllib2.urlopen(url, None, 20)
        r = opener.open(url, None, 20)    
        r2 = r.read()
        print "="*40
        ch = chardet.detect(r2)
        print ch
        print r2
        #print r2.decode("gbk")
    except IOError, e:
        print e
        
def func3():
    f_in = "open('/home/joe/file.txt', 'rb')"
    f_out = gzip.open(ur'd:\file.txt.gz', 'wb')
    f_out.writelines(f_in)
    f_out.close()

def func4():
    f = gzip.open(ur'd:\file.txt.gz', 'rb')
    file_content = f.read()
    f.close()
    print file_content

def func5():
    proxy_support = urllib2.ProxyHandler({'http':'212.156.150.130:8080'})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    try:
        url = u"http://www.microbell.com/docdetail_662667.html"
        r = urllib2.urlopen(url)    
        r2 = r.read()
        r3 = gzip.GzipFile(fileobj=StringIO.StringIO(r2)).read()
        print "="*40
        ch = chardet.detect(r3)
        print ch
        print r3.decode("gbk")
    except IOError, e:
        print e
        
def func6():
    proxy_support = urllib2.ProxyHandler({'http':'61.187.64.20:80'})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    #urllib2.install_opener(opener)
    try:
        fullurl = u"http://www.baidu.com"
        r=opener.open(fullurl, data=None, timeout=20)
        print "use proxy:"
        print r.headers
    except IOError, e:
        print e
        
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    try:
        fullurl = u"http://www.baidu.com"
        r=opener.open(fullurl, data=None, timeout=20)
        print "not use proxy:"
        print r.headers
    except IOError, e:
        print e
    

if __name__ == '__main__':
    func6()
