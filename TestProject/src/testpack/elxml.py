#-*- coding:utf-8 -*-
'''
Created on 2011-11-4

@author: GFTOwenWang
'''
from lxml import etree



def hello(dummy, b, c):
    return "Hello %s and %s" % (b, c)

def ola(dummy, b):
    return "Ola %s" %b

def loadsofargs(dummy, *args):
    return "Got %d arguments." % len(args)

def compare(dummy, str1, str2):
    print "a:(%s)%s, b:(%s)%s" %(type(str1[0]),str1[0],type(str2), str2)
    r = cmp(str1[0], unicode(str2))
    return r




def test_func1():
    ns = etree.FunctionNamespace(None)
    ns["hello"] = hello
    ns["countargs"] = loadsofargs
    
    root = etree.XML("<a><b>Haegar</b></a>", parser=None, base_url=None)
    doc = etree.ElementTree(element=root, file=None, parser=None)
    
    print(root.xpath("hello('world', 'o')"))
    print(root.xpath("hello(local-name(*),'0')"))
    print(root.xpath('hello(string(b), 0)'))
    print(root.xpath('countargs(., b, ./*)'))
    
    
    ns2 = etree.FunctionNamespace('http://mydomain.org/myother/functions')
    ns2.prefix = 'es'
    ns2['hello'] = ola
    print(root.xpath('es:hello(local-name(*))'))
    
def test_func2():
    ns = etree.FunctionNamespace("http://mydomain.org/myother/functions")
    ns.prefix = 'gs'
    ns["hello"] = hello
    ns["compare"] = compare
    
    file = open(r"d:\test\xml\books.xml")
    xml = etree.XML(file.read())
    file.close()
    
    print xml.xpath("gs:hello('world', 'o')")
    
    file = open(r"d:\test\xml\book.xslt")
    xslt = etree.XML(file.read())
    file.close()
    transfer = etree.XSLT(xslt)
    result = transfer(xml)
    
    print result
    
if __name__ == '__main__':
    #test_func1()
    test_func2()
#    r = compare2(None, 'a','b')
#    
#    print type(r)
#    print r
    
    