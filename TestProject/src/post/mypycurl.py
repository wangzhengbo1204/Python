'''
Created on 2011-10-10

@author: GFTOwenWang
'''
import pycurl

c = pycurl.Curl()
c.setopt(c.POST, 1)
c.setopt(c.URL, "http://192.168.1.22:8080/lavazza_doc/fileInfo.api?med=upload&nickName=bbb")
c.setopt(c.HTTPPOST, [("file1", (c.FORM_FILE, "d:\\doc.txt"))])
#c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
print "that's it ;)"