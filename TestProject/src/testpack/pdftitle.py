#-*- coding:utf-8 -*-
'''
Created on 2011-11-4

@author: GFTOwenWang
'''

from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file(ur"d:\test\pdf\FL00002D0J.pdf", "rb"))

# print the title of document1.pdf
print "title = %s" % (input1.getDocumentInfo().title)