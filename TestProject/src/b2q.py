# -*- coding:utf-8 -*-
'''
Created on 2011-8-12

@author: GFTOwenWang
'''

def strQ2B(ustring):
    """把字符串全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code==0x3000:
            inside_code=0x0020
        else:
            inside_code-=0xfee0
        if inside_code<0x0020 or inside_code>0x7e:      #转完之后不是半角字符返回原来的字符
            rstring += uchar
        rstring += unichr(inside_code)
    return rstring

a=u'a•b.txt'
b= strQ2B(a)
print b