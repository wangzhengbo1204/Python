#-*- coding:utf-8 -*-
'''
Created on 2012-3-30

@author: GFTOwenWang
'''
import urllib
import urllib2
import cookielib
import os


def login():
    pass

def func1():
    url = "http://www.ccxi.com.cn/RedirectDown.do?cid=01-01d&id=2319&bondcode="
    #opener = urllib2.build_opener()
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(httpcookie, urllib2.HTTPHandler)
    
    if True:
        url_login = "http://www.ccxi.com.cn/LoginCheck.html?action=login"
        postdata = (tuple("username:gftchina".split(":")), 
                    tuple("password:gftchina".split(":")), 
                    ("Submit", "Login"))
        request = urllib2.Request(url_login, urllib.urlencode(postdata))
        opener.open(request)
    opener.addheaders = [('User-agen', 'MSIE/6.0')]
        
    r = opener.open(url, None, 20)
    
    s = r.read()
    print s.decode('gbk')
    
def func2():
    url = 'http://www.chinamoney.com.cn/fe-c/interestRateSwapCurveHistoryAction.do'
    url = urllib.quote(url, ':/.&=?')
    r = urllib2.urlopen(url)
    print r.headers
#    s = r.read()
#    print s.decode('utf-8')
#    
    
def func3():
    url = 'http://view.microbell.com/download.asp?fileurl=/UpFile/2012_9/201297111716530.pdf'  
    r = urllib2.urlopen(url, None, None)
    content = r.headers["Content-Disposition"]
    print 'ok'
    
    url = 'http://www.baidu.com'  
    r = urllib2.urlopen(url, None, None)
    content_type = r.headers["Content-Type"]
    if content_type.startswith("text/html"):
        filetype ="html"
    else:
        if "Content-Disposition" in r.headers:
            disposition  = r.headers["Content-Disposition"]
            filename = r.headers["Content-Disposition"][len("attachment;filename="):].replace('"','')
            splitext = os.path.splitext(filename)
            if splitext:
                filetype = splitext[1]
            else:
                filetype = "html"
    print 'ok'  
    
def func4():
    url = 'http://jingzhi.funds.hexun.com/fb/zhejia.htm'
    filename=ur'd:\xinxi.htm'
    urllib.urlretrieve(url, filename)
    urllib2.urlopen(url, None, None)
    
def func5():
    url = "http://jingzhi.funds.hexun.com/fb/zhejia.aspx"
    #url = "http://www.baidu.com/"
    #opener = urllib2.build_opener()
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(httpcookie, urllib2.HTTPHandler)
    
    postdata = (("fund_com",""),("enddate","2012-11-19"))
    #request = urllib2.Request(url, urllib.urlencode(postdata))
    pd = urllib.urlencode(postdata)
    
    opener.addheaders = [('User-agen', 'MSIE/6.0')]
        
    r = opener.open(url, data=pd, timeout=20)
    #r = opener.open(url)
    
    s = r.read()
    f=open(ur'd:\a.html',"wb")
    f.write(s)
    f.close()
    print s.decode('gbk')
    
if __name__ == '__main__':
    func5()
    