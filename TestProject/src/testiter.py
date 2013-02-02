#-*- coding:utf-8 -*-
'''
Created on 2012-7-30

@author: GFTOwenWang
'''
import urllib2
from lxml import etree, html
from gftdata.share.support.data.proxylistprovider import ProxyListProvider


def parse(url, charset):
    response = urllib2.urlopen(url, timeout=20)
    strfile = response.read()
    strfile = strfile.decode(charset)
    
    root = html.fromstring(strfile)
    value = root.xpath("//div[@id='proxylisttb']/table[3]//tr")
    list_records = []
    print "lenght of proxy: %s" % len(value)
    for item in value[1:]:
        if item:
            ip,port = item.xpath("td[1]/text()").split(':')
            protocol = item.xpath("td[2]/text()")
            country = item.xpath("td[4]/text()")
            disabletimes = 0
            is_valid = testing_proxy(ip, port)
            if is_valid:
                print "valid %s:%s" %(ip, port)
                proxyListProvider = ProxyListProvider()
                proxyListProvider = ProxyListProvider(proxyListProvider.record_id,
                                                      ip, port,protocol, None,
                                                      country,disabletimes)
                proxyListProvider.save()
            else:
                print "invalid %s:%s" %(ip, port)
        
    

class Fib:  
    def __init__(self, max):  
        self.max = max  
        self.a = 0  
        self.b = 1  
          
    def __iter__(self):  
#        self.a = 0  
#        self.b = 1  
        return self  
      
    def next(self):  
        fib = self.a  
        if fib > self.max:  
            raise StopIteration # 如果已经大于最大值则抛出StopIteration异常  
        self.a, self.b = self.b, self.a + self.b # 在return之前将self的值更新  
        return fib  
      
class IterURL(object):
    
    def __init__(self, baseurl, charset):
        self.baseurl = baseurl #http://www.sse.com.cn/sseportal/webapp/datapresent/ZQPartEnterpriseBondBasicInfoAct?reportName=BizCompPartEnterpriseBondBasicInfoRpt&EBOND_CODE=125014
        self.charset = charset
        self.code = 125010
        self.url = None
        
    def __iter__(self):
        return self
    
    def next(self):
        try_count = 0
        while try_count<3:
            url = u"%s&EBOND_CODE=%s" % (self.baseurl, self.code)
            response = urllib2.urlopen(url, timeout=20)
            strfile = response.read()
            strfile = strfile.decode(self.charset)
            
            root = html.fromstring(strfile)
            value = root.xpath("//table[@class='content']/tr[1]/td[2]/text()")
            
            self.code = self.code + 1
            
            if value:
                self.url = url
                return url
            
            try_count += 1
        else:
            raise StopIteration
        
    def urls(self):
        try_count = 0
        while try_count<3:
            url = u"%s&EBOND_CODE=%s" % (self.baseurl, self.code)
            response = urllib2.urlopen(url, timeout=20)
            strfile = response.read()
            strfile = strfile.decode(self.charset)
            
            root = html.fromstring(strfile)
            value = root.xpath("//table[@class='content']/tr[1]/td[2]/text()")
            
            self.code = self.code + 1
            
            if value:
                self.url = url
                yield url
            else:
                try_count += 1
        else:
            raise StopIteration
    

def test_fib():
    fib = Fib(1000)  
    for n in fib:  
        print n  
        
def test_iterurl():
    iterURL = IterURL("http://www.sse.com.cn/sseportal/webapp/datapresent/ZQPartEnterpriseBondBasicInfoAct?reportName=BizCompPartEnterpriseBondBasicInfoRpt",'gbk')  
    for n in iterURL.urls():  
        print n
        
if __name__=="__main__":  
    test_iterurl()
    
    