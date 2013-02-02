'''
Created on 2012-8-21

@author: GFTOwenWang
'''
import cookielib
import os
import urlparse
import urllib
import urllib2


BROWER_AGENT=('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0')

def create_new_opener():
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)

    opener = urllib2.build_opener(httpcookie, urllib2.HTTPHandler)
    
    #self.opener.addheaders = [('User-agent', random.choice(BROWER_AGENT))]
    opener.addheaders = [('User-agent', BROWER_AGENT)]
    return opener

def read():
    #url = "http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemoreinfolist.jsp?pathId=18612&conditions=id+%3E+0+and+path+like+%27%25%B8%B6%CF%A2%B6%D2%B8%B6%D3%EB%D0%D0%C8%A8%B9%AB%B8%E6%25%27&title=%B8%B6%CF%A2%B6%D2%B8%B6%D3%EB%D0%D0%C8%A8%B9%AB%B8%E6&_tp_t1213154157187=1"
    url = "http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemoreinfolist.jsp?pathId=18612&form_salescompany=&form_issuepersonal=&form_issueyear=&form_issuenum=&form_keyword=&title=%B8%B6%CF%A2%B6%D2%B8%B6%D3%EB%D0%D0%C8%A8%B9%AB%B8%E6"
    if isinstance(url, unicode):
        url = url.encode('utf-8')
    
    url = urllib.unquote(url)
    url = urllib.quote(url, safe=':/?&=')
        
    opener = create_new_opener()
    r = opener.open(url, data=None, timeout=20)
    
    f = open(r"D:\GFT\FileServer\RawFiles\Web\2012-08-21\a.html", 'wb')
    text = r.read()
    f.write(text)
    f.close()
    
def test_func2():
    url = "http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemoreinfolist.jsp?pathId=18612&form_salescompany=&form_issuepersonal=&form_issueyear=&form_issuenum=&form_keyword=&title=%B8%B6%CF%A2%B6%D2%B8%B6%D3%EB%D0%D0%C8%A8%B9%AB%B8%E6"
    url2 = urllib.unquote(url)
    url3 = urllib.quote(url2, ":?/=&")
    print url3
    
    urlobj = urlparse.urlparse(url)
    print urlobj
    path= urllib.quote(urlobj.path)
    url4 = urlparse.urlunparse((urlobj.scheme,urlobj.netloc,path,
                               urlobj.params,urlobj.query, urlobj.fragment))
    print url4
    
    r=urllib2.urlopen(url4, None, 20)
    text =r.read()
    f =open(ur"D:\GFT\FileServer\RawFiles\Web\2012-08-21\b.html",'wb')
    f.write(text)
    f.close()

if __name__ == "__main__":
    read()
    #test_func2()
    