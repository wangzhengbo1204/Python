# -*- coding: utf-8 -*-
#############################################
## (C)opyright by Dirk Holtwick            ##
## All rights reserved                     ##
#############################################

__version__ = "$Revision: 176 $"
__author__ = "$Author: kgrodzicki $"
__date__ = "$Date: 2011-01-15 10:11:47 +0100 (Fr, 15 July 2011) $"

"""
HTML/CSS to PDF converter
Test for support left/right (even/odd) pages
"""
from xhtml2pdf.parser import HTML2PDF
#from parser import HTML2PDF
#import parser.HTML2PDF as HTML2PDF

if __name__ == "__main__":
    xhtml = open(r'D:\test\chinabond.html')
    HTML2PDF("", xhtml.read(), xml_output="testEvenOdd.pdf")
