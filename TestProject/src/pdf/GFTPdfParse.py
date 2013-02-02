#-*- coding:utf-8 -*-
'''
Created on 2012-2-29
@author: laigen
'''

import sys
import os
from binascii import b2a_hex
import re

from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar , LTTextBoxHorizontal , LTText , LTAnon , LTPage , LTLine

#debug
import codecs
debug_file = codecs.open("debug.txt", 'w',"utf-8")
#end debug

class GFTPdfString :
    ''' 在Pdf中输出的文字信息 '''
    def __init__(self):
        self.str = "" ;
        self.page_num = 0 ;
        self.font_name = "" ;
        self.font_size = 0.0 ;
        self.x0 = 0.0 ;
        self.y0 = 0.0 ;
        self.x1 = 0.0 ;
        self.y0 = 0.0 ;
        
def pdf_object_sort(o1,o2):
    return o1.x0 + (5000-o1.y1) > o2.x0 + (5000-o2.y1) ;

class GFTPdfParse(object) :
    ''' 针对pdf研报文件的拆解 '''
    def __init__(self):
        self.guess_title = "" ; #猜测的文章标题
        #
        self.possible_titles = []
        #
        self.author = [] ; #监控而得到的针对性的研究员信息
        self.data_table = [] ;#数据表的内容项
        self.figure = [] ; #研报中引用到的图片
        self.content = "" ; #研报中的所有正文文字
        self.lsStr = [] ; #value为GFTPdfString
    
    def add_possible_title(self, str, height, width):
        value = height ** 2 + width
        self.possible_titles.append((str, value))
        self.possible_titles = sorted(self.possible_titles, key=lambda pair: pair[1], reverse=True)
        if len(self.possible_titles) > 5:
            del self.possible_titles[5]
  
    def get_all_sub_class(self, lt_obj, class_type, lsRlt):
        """
            lt_obj: parent obj
            class_type: sub class type
            lsRlt: out put list 
        """
        if "__iter__" in dir(lt_obj) :
            for obj in lt_obj :
                if isinstance(obj , class_type) :
                    lsRlt.append(obj) ;
                else :
                    self.get_all_sub_class(obj , class_type , lsRlt) ;
                    
    def chg_pdf_coord(self,pdfobj,pgHeight):
        return (pdfobj.x0 , pgHeight - pdfobj.y1 , pdfobj.x1 , pgHeight - pdfobj.y0 ) ;
    
    def parse_pdf(self,filepath,pdf_pwd=''):
        ''' 解析pdf '''
        # open the pdf file
        fp = open(filepath, 'rb')
        # create a parser object associated with the file object
        parser = PDFParser(fp)
        # create a PDFDocument object that stores the document structure
        doc = PDFDocument()
        # connect the parser and document objects
        parser.set_document(doc)
        doc.set_parser(parser)
        # supply the password for initialization
        doc.initialize(pdf_pwd)

        #if doc.is_extractable:
            # apply the function and return the result
        self._parse_pages(doc) ;
        pass ;

        # close the pdf file
        fp.close()
        
    def _parse_pages (self , doc):
        """With an open PDFDocument object, get the pages and parse each one
            [this is a higher-order function to be passed to parse_pdf()]"""
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
    
        text_content = []
        for i, page in enumerate(doc.get_pages()):
#            try:
            interpreter.process_page(page)
            # receive the LTPage object for this page
            layout = device.get_result()
            # layout is an LTPage object which may contain child objects like LTTextBox, LTFigure, LTImage, etc.
            self._parse_lt_objs(layout, (i+1)  ) ;
#            except Exception, e:
#                print >> debug_file, "error parsing page ", (i+1), "%s" % (os.linesep)
#                print >> debug_file, sys.exc_info()[0]
        if self.lsStr :
            self.content = "\r\n".join(o.str for o in self.lsStr ) ;
            
    def _parse_lt_objs (self,lt_objs, page_number ):
        """Iterate through the list of LT* objects and capture the text or image data contained in each"""
        page_text = [] # k=(x0, x1) of the bbox, v=list of text strings within that bbox width (physical column)
        
        pg_height = lt_objs.y1 ;
        
        for lt_obj in lt_objs:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                # text, so arrange is logically based on its column width
                self._ana_textinfo(page_text, lt_obj,pg_height) ;
            elif isinstance(lt_obj, LTImage):
                # an image
                pass ;
            elif isinstance(lt_obj, LTFigure):
                # LTFigure objects are containers for other LT* objects, so recurse through the children
                #self._parse_lt_objs(lt_obj, page_number) ;
                #self._ana_lineinfo(page_text, lt_obj,pg_height) ;
                pass ;
            elif isinstance(lt_obj, LTLine):
                # LTFigure objects are containers for other LT* objects, so recurse through the children
                #self._parse_lt_objs(lt_obj, page_number) ;
                
                pass ;
        
        lsTxt = [] ;
        maxFontSize = 0 ;
        
        peAuthor = re.compile(r"(S\d{13})") ;
        #peTableChart = re.compile(ur"(^[图表]{1,}格{0,}\s*[\d一二三四五六七八九十]{1,}[:|：]*\s*\S*)") ;
        peTableChart = re.compile(ur"(^[图表]{1,}格{0,}\s*[\d一二三四五六七八九十]{1,}[:|：]*[\s\S])") ;
        peTable = re.compile(ur"([^图]附*表+格*[\s\t]*[\d一二三四五六七八九十]+[:|：]*\s*\S*)")
        for o in page_text :
            if o.str and len(o.str.strip()) > 0 :
                #print >>debug_file, "%s(x0=%d,y0=%d,w=%d,h=%d,pg=%d)%s"%(o.str,o.x0 , o.y0 , o.x1-o.x0 , o.y1-o.y0,page_number,os.linesep) ;
                
                if page_number == 1 :
                    #按照字体大小，来决定文章的标题
                    #if o.font_size > maxFontSize :
                    self.add_possible_title(o.str.strip(), abs(o.y1 - o.y0), abs(o.x1 - o.x0))
                    self.guess_title = self.possible_titles[0][0]
                        #self.guess_title = o.str.strip() ;
                       # maxFontSize = o.font_size ;
                    lsAna = peAuthor.findall(o.str.strip()) ;
                    if lsAna :
                        for au in lsAna :
                            self.author.append(au) ;
                lsChart = peTableChart.findall(o.str.strip()) ;
                if lsChart :
                    for ch in lsChart :
                        self.data_table.append(ch) ;
                    #if peTable.findall(o.str):
                    #    print "table found at", page_number
                    #    print "table name: ", o.str
                o.page_num = page_number ;
                lsTxt.append(o) ;
                self.lsStr.append(o) ;
        '''    
        if page_number == 1 :
            for o in lsTxt :
                print "<" + str(o.x0) + "," + str(o.y0) + ">" + o.str + "("+str(o.font_size)+")" ; 
        '''
    
        #for k, v in sorted([(key,value) for (key,value) in page_text.items()]):
            # sort the page_text hash by the keys (x0,x1 values of the bbox),
            # which produces a top-down, left-to-right sequence of related columns
            #text_content.append(''.join(v))
            
    
                
    def _ana_textinfo(self,h, lt_obj, pg_height ):
        ''' 分析文本信息，拆解出标题和一整段的文字 '''
        lsLTChar = [] ;
        self.get_all_sub_class(lt_obj,LTChar,lsLTChar) ;
        
        pct=0.5 ;
        lsLTChar.sort(pdf_object_sort) ;
        
        for c in lsLTChar :
            if len(c.get_text()) == 0 :
                continue ;
            key_found = False ;
            (x0,y0,x1,y1) = self.chg_pdf_coord(c,pg_height) ; #PDF的坐标轴是反向的，所以必须做一层转换
            #print >>debug_file, c.get_text(), (x0,y0,x1,y1)
            #print >>debug_file, "\r\n"
            if h :
                for o in h :
                    rev = o.font_size * pct ;
                    
                    if x0 >= (o.x1-rev*4) and x0 <= (o.x1 +rev*4) and \
                        y0 >= (o.y0-c.size/2) and y0 <= (o.y0 + c.size/2) \
                        and y1 >= (o.y1 - c.size/2) and y1 <= (o.y1 + c.size/2)\
                         and abs(c.size - o.font_size) <= max(c.size , o.font_size)*2.0/3.0 :
                        o.str = o.str + c.get_text() ;
                        o.x0 = min(o.x0,x0) ;
                        o.x1 = max(o.x1,x1) ;
                        o.y0 = min(o.y0,y0) ;
                        o.y1 = max(o.y1,y1) ;
                        key_found = True ;
                        break ;
            if not key_found :
                curChar = GFTPdfString() ;
                curChar.str = c.get_text() ;
                curChar.font_name = c.fontname ;
                curChar.font_size = c.size ;
                curChar.x0 = x0 ;
                curChar.y0 = y0 ;
                curChar.x1 = x1 ;
                curChar.y1 = y1 ;
                h.append(curChar) ;
        #debug code
        print >>debug_file, os.linesep.join([("string: " +c.str + os.linesep + \
                                               "\t font_size:" + str(c.font_size) + os.linesep)for c in h])
#                                               "\t font_name:" + c.font_name) + os.linesep)for c in h])
        
    def _ana_lineinfo(self,h,lt_obj,pg_height):
#        lsLTLine = [] ;
#        self.get_all_sub_class(lt_obj,LTLine,lsLTLine) ;
#        
#        lsLTLine.sort(pdf_object_sort) ;        
        pass ;

def test():
    p = GFTPdfParse() 
    p.parse_pdf(r"c:\test3.pdf") 
    return p.content
        
if __name__=='__main__':  
    p = GFTPdfParse() ;
    p.parse_pdf(r"c:\Reports\P020111014519337789944.pdf") ;
#    p.parse_pdf(r"c:\test3.pdf") ;
    print  p.guess_title ;
    print  p.author ;
    if p.data_table :
        print "获取的内容："
        for t in p.data_table :
            print unicode(t) ;
    print p.content ;
    

    
    #s1 = u"图表1：月度进、出口同比（单位：%）     表2：月度进、出口同比（单位：%）  " ;
    
    #pe = re.compile(r"([图表]{1,}\d(1,)[:|：]*\s*\S*)") ;
    #pe = re.compile(ur"([图表]{1,}\s*[\d一二三四五六七八九十]{1,}[:|：]*\s*\S*)") ;
    
    #print pe.findall(s1) ;
    