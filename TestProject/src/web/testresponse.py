'''
Created on 2012-4-26

@author: GFTOwenWang
'''
import urllib2


def func1():
    try:
        url = "http://www.microbell.com/docdetail_685649.html"
        
        proxy = urllib2.ProxyHandler({"http":"85.117.39.98:8080"})
        opener = urllib2.build_opener(proxy, urllib2.HTTPHandler)
        r = opener.open(url, None, 20)
        #r = urllib2.urlopen(url, None, 20)
        s =r.read()
        print s
    except urllib2.HTTPError as ex:
        print ex
    
    
if __name__ == "__main__":
    func1()
    