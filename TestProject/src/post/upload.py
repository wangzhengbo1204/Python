# -*- coding:utf-8 -*-
'''
Created on 2011-9-30

@author: GFTOwenWang
'''
import MultipartPostHandler, urllib2, cookielib

#cookies = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
#MultipartPostHandler.MultipartPostHandler)
##params = { "username" : "", "password" : "riviera","meds":"upload",
##"uploadFiles" : open(r"d:\doc1.txt", "rb") }
#
##params = {"med":"upload","uploadFile" : open(r"d:\doc1.txt", "rb") }
##u = opener.open("http://192.168.1.22:8080/lavazza_doc/fileInfo.api", params)
#
#u = opener.open("http://192.168.1.22:8080/lavazza_doc/fileInfo.api?med=upload", open(r"d:\doc1.txt", "rb"))
#
#print u 

params = {"med":"download","id":"49", "isStream" : "true"}
cookies = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
MultipartPostHandler.MultipartPostHandler)
#params = { "username" : "", "password" : "riviera","meds":"upload",
#"uploadFiles" : open(r"d:\doc1.txt", "rb") }

#params = {"med":"upload","uploadFile" : open(r"d:\doc1.txt", "rb") }
#u = opener.open("http://192.168.1.22:8080/lavazza_doc/fileInfo.api", params)

u = opener.open("http://192.168.1.22:8080/lavazza_doc/fileInfo.api", params)

file = open(r"d:\49.pdf", "wb")

file.write(u.read())
print u 