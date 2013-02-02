# -*- coding:utf-8 -*-
'''
Created on 2011-11-10

@author: GFTOwenWang
'''
import urllib2
import httplib
import cookielib
import urllib


def http_server():
    import SimpleHTTPServer
    import SocketServer
    
    PORT = 9090
    
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    
    print "serving at port", PORT
    httpd.serve_forever()
    
def test_urlopen():
    import urllib
    params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    url = "http://www.lianheratingss.com.cn"
    f = urllib.urlopen(url)
    s = f.read()
    print s
    urllib.urlretrieve( url, 'urlre.html' )
    
def test_urlopen2():
    import urllib2
    url = "http://www.shclearing.com/UpLoadFiles/Market/2011-11/122%E3%80%81%E4%B8%AD%E5%9B%BD%E5%8C%96%E5%B7%A5%E9%9B%86%E5%9B%A2%E5%85%AC%E5%8F%B82011%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E6%9C%9F%E7%9F%AD%E6%9C%9F%E8%9E%8D%E8%B5%84%E5%88%B8%E5%8F%91%E8%A1%8C%E5%85%AC%E5%91%8A.pdf"
    f = urllib2.urlopen(url)
    s = f.read()
    print s
    
def test_urlopen3():
    import urllib2
    url = "http://www.shclearing.com/UpLoadFiles/Market/2011-11/122%E3%80%81%E4%B8%AD%E5%9B%BD%E5%8C%96%E5%B7%A5%E9%9B%86%E5%9B%A2%E5%85%AC%E5%8F%B82011%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E6%9C%9F%E7%9F%AD%E6%9C%9F%E8%9E%8D%E8%B5%84%E5%88%B8%E5%8F%91%E8%A1%8C%E5%85%AC%E5%91%8A.pdf"
    req = urllib2.Request(url,
                       data='This data is passed to stdin of the CGI')

    f = urllib2.urlopen(req)
    s = f.read()
    print s
    
def test_urlopen4():
    import httplib
    url = "http://www.shclearing.com"
    conn = httplib.HTTPConnection("www.shclearing.com")
    conn.request("GET", "http://www.shclearing.com/UpLoadFiles/Market/2011-11/%E5%B9%BF%E8%A5%BF%E7%8E%89%E6%9F%B4%E6%9C%BA%E5%99%A8%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B82011%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%89%E6%9C%9F%E7%9F%AD%E6%9C%9F%E8%9E%8D%E8%B5%84%E5%88%B8%E5%8F%91%E8%A1%8C%E5%85%AC%E5%91%8A.pdf")
    r1 = conn.getresponse()
    print r1.status, r1.reason
    print r1
    
def test_urlopen5():
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(httpcookie)
    opener.addheaders=[('User-agen','MSIE/6.0')]
    urllib2.install_opener(opener)
    
    f = opener.open("http://www.ccxi.com.cn/RedirectDown.do?cid=01-01d&Organcode=7b29054892cb44fa9407a0b3cad27adc&downClass=body&RatingDate=", data=None, timeout=10)
    print f.read()
    
def test_urlopen6():
    url = 'http://www.shclearing.com/UpLoadFiles/Market/2011-9/中国联合网络通信有限公司2011年度第四期超%20短期融资券发行公告.pdf'
    #urllib.urlretrieve(url, r'd:\test\a.pdf')
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(httpcookie)
    opener.addheaders=[('User-agen','MSIE/6.0')]
    urllib2.install_opener(opener)
    url = urllib.unquote(url)
    print url
    url = urllib.quote(url, safe=':/')
    print url
    f = opener.open(url, data=None, timeout=10)
    print f.read()
    
class BaiduBlog:

    def __init__(self):
        cookie = cookielib.CookieJar()
        self.httpcookie = urllib2.HTTPCookieProcessor(cookie)

    def login(self,username,password):
        url='http://www.ccxi.com.cn/LoginCheck.html?username=gftchina&password=gftchina&action=login'
        postdata= (("name",username),("psw",password),("Submit"," 登录 "))
        self.opener = urllib2.build_opener(self.httpcookie)
        self.opener.addheaders=[('User-agen','MSIE/6.0')]
        urllib2.install_opener(self.opener)
        request = urllib2.Request(url,urllib.urlencode(postdata))
        urllib2.urlopen(request)

    def visit(self,url):
        conn = httplib.HTTPConnection("www.dagongcredit.com")
        conn.request("GET", "/dagongweb/uploadfile/20110803092359.pdf")
        r1 = conn.getresponse()
        print r1.status, r1.reason
        print r1
        f = self.opener.open(url)
        bloghtml = f.read()
        print bloghtml
        f.close()
        
    def test1(self):
        pass
    
class DaGong:

    def __init__(self):
        cookie = cookielib.CookieJar()
        self.httpcookie = urllib2.HTTPCookieProcessor(cookie)

    def login(self,username,password):
        url='http://www.dagongcredit.com/dagongweb/reg/log_index.php'
        postdata= (("naame1",username),("psaw2",password),("Submit"," 登录 "))
        self.opener = urllib2.build_opener(self.httpcookie)
        self.opener.addheaders=[('User-agen','MSIE/6.0')]
        urllib2.install_opener(self.opener)
        request = urllib2.Request(url,urllib.urlencode(postdata))
        urllib2.urlopen(request)

    def visit(self,url):
        conn = httplib.HTTPConnection("www.dagongcredit.com")
        conn.request("GET", "/dagongweb/uploadfile/20110803092359.pdf")
        r1 = conn.getresponse()
        print r1.status, r1.reason
        print r1
        f = self.opener.open(url)
        bloghtml = f.read()
        print bloghtml
        f.close()
        
    def test1(self):
        pass
    
if __name__ == '__main__':
    #test_urlopen3()
    
#    username = '201218'
#    password = '201218'
#    url = 'http://www.dagongcredit.com/dagongweb/uploadfile/20110803092359.pdf'
#    bb = BaiduBlog()
#    bb.login(username,password)
#    bb.visit(url);
#    
    test_urlopen5()

