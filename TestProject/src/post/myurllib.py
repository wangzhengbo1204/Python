'''
Created on 2011-10-10

@author: GFTOwenWang
'''

import httplib, urllib, codecs


def upload():
    #params = {"med":"upload","nickName":"bbbbb", "uploadFile" : open(r"d:\doc1.txt", "rb") }
    #params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    #headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("192.168.1.22:8080")
    #conn.request("POST", "/lavazza_doc/fileInfo.api", params, headers)
    
    file = open(r"d:\FL000022JK.pdf", "rb")
    #s = codecs.StreamReader(file)
    #s1= s.readlines()
    conn.request("POST", "/lavazza_doc/fileInfo.api?med=upload&nickName=i&fileType=.pdf", file)
    response = conn.getresponse()
    print response.status, response.reason
    print response.read()
    data = response.read()
    conn.close()

def download():
    #params = {"med":"upload","nickName":"bbbbb", "uploadFile" : open(r"d:\doc1.txt", "rb") }
    #params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    #headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("192.168.1.22",8080)
    #conn.request("POST", "/lavazza_doc/fileInfo.api", params, headers)
    
    #file = open(r"d:\49.pdf", "rb")
    #s = codecs.StreamReader(file)
    #s1= s.readlines()
    #params = {"med":"download","id":"49", "isStream" : "true"}
    params = "med=download&id=56&isStream=true"
    u=conn.request("POST", "/lavazza_doc/fileInfo.api", params)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    file = open(r"d:\56.pdf", "wb")
    file.write(data)
    conn.close()
    
def download2():
    #params = {"med":"upload","nickName":"bbbbb", "uploadFile" : open(r"d:\doc1.txt", "rb") }
    #params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    #headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("192.168.1.22:8080")
    #conn.request("POST", "/lavazza_doc/fileInfo.api", params, headers)
    
    #file = open(r"d:\49.pdf", "rb")
    #s = codecs.StreamReader(file)
    #s1= s.readlines()
    #params = {"med":"download","id":"49", "isStream" : "true"}
    params = "med=download&id=56&isStream=true"
    u=conn.request("POST", "/lavazza_doc/fileInfo.api?med=download&id=56&isStream=true")
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    file = open(r"d:\56.pdf", "wb")
    file.write(data)
    conn.close()
    

if __name__ == '__main__':
    #upload()
    #download()
    download2()
    
    