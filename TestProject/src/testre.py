# -*- coding:utf-8 -*-
'''
Created on 2011-11-18

@author: GFTOwenWang
'''
import re

def test_func1():
    a=r"^abc.*\.xls$"
    b="abc2011-11-18.xls"
    r = re.compile(a)
    g = r.search(b)
    print g
    
def test_func2():
    a=r"^中期票据.*\.xls$"
    b="中期票据2011-11-18.xls"
    r = re.compile(a)
    g = r.search(b)
    print g
    
def test_func3():
    a = r"2011-10-19 15:40:47.140000"
    p=r".\d{4,}"
    r=re.compile(p)
    g=r.search(a)
    if g:
        print g.group()
        
def test_func4():
    a=u'71超短期融资券.xml'
    b=u"(\d*)"
    r = re.compile(b)
    g = r.search(a)
    if g:
        print g.group()
    else:
        print None
    
def test_func5():
    a=r"2011年记账式附息(二期)国债".replace("(", "\\(").replace(")", "\\)")
    b="2011年记账式附息(二期)国债"
    r = re.compile(a)
    g = r.search(b)
    print g
    
def test_func6():
    a=r"abc123@gftchina.com"
    b=r"^\.*"
    #b=r"^.*$"
    p = re.compile(b)
    g=p.search(a)
    print g
    
def test_func7():
    a="{5a}"
    b=r"{(\d+)}"
    r= re.compile(b)
    g = r.match(a)
    print g
    print g.group(1)
    
def test_func8():
    p = "\d$"
    a="Bon1dD"
    r = re.compile(p)
    g = r.search(a)
    print g
    print g.group(1)
    
def test_func9():
    p = re.compile('(?<={)(\d+)(?=})')
    #p = re.compile('{(\d+)}')
    s = "{1}+{2}/{3}"
    g = p.search(s)
    print len(g)
    
def test_func10():
    marketcode = r'([A-Za-z]*)'
    listid = r'(\d*)'
    p1 = re.compile(marketcode)
    print p1
    print p1.search('CBOTC7094').group(0)
    
    p2 = re.compile(marketcode)
    print p2
    print p2.search('CBOTC7094').group(0)
    
def test_func11():
    pattern = r'.*(?=\d+\.\d+)'
    r = re.compile(pattern)
    a= 'CFETS.IRS-FR007-Closing-Mid.Par7.0000'
    g = r.search(a)
    print g
    
def test_func12():
    pattern=r"(\d+)$"
    r = re.compile(pattern)
    a="MMax3"
    g = r.search(a)
    if g:
        print g.groups()
        
    g2 = r.match(a)
    if g2:
        print g2.groups()

if __name__ == "__main__":
    test_func12()
    