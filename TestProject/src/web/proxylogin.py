'''
Created on 2012-3-28

@author: GFTOwenWang
'''
import urllib
import urllib2
import cookielib
import gzip
import StringIO
from datetime import datetime


#proxy_handler = urllib2.ProxyHandler({'http': 'http://www.example.com:3128/'})
#proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
#proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
#
#opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
## This time, rather than install the OpenerDirector, we use it directly:
#opener.open('http://www.example.com/login.html')


def create_opener():
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(httpcookie)
    opener.addheaders = [('User-agen', 'MSIE/6.0')]
    
    proxy_support = urllib2.ProxyHandler({'http':'109.109.42.2:8080'})
    #proxy_support = None
    opener = urllib2.build_opener(httpcookie, 
                                  proxy_support, 
                                  urllib2.HTTPHandler)

    return opener
    
def login(opener, url, user, password):
    postdata = (tuple(user.split(":")), tuple(password.split(":")), ("Submit", "Login"))
    request = urllib2.Request(url, urllib.urlencode(postdata))
    #urllib2.urlopen(request)
    opener.open(request)
    
def func1(url, postdata=None, timeout=20):
    opener = create_opener()
    print datetime.now()
    try:
        r = opener.open(url, postdata, timeout)
        s = r.read()
        print s
    except Exception as ex:
        print ex
    finally:
        print datetime.now()
    
def func2(url, postdata=None, timeout=20):
    opener = create_opener()
    login(opener, "http://www.microbell.com/toploginnew.asp?action=login",
          "name:gfttech","pwd:gfttech")
    print datetime.now()
    try:
        r = opener.open(url, postdata, timeout)
        s = r.read()
        s2 = gzip.GzipFile(fileobj=StringIO.StringIO(s)).read()
        print s2
    except Exception as ex:
        print ex
    finally:
        print datetime.now()

if __name__ == "__main__":
    url = "http://www.microbell.com/docdetail_666361.html"
    func1(url)