#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
Created on 2012-3-19
'''
import sys, os, re
###
### pdf-miner requirements
###
from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar , LTTextBoxHorizontal , LTText , LTAnon , LTPage , LTLine

'''
skeleton
'''

class pdfMinerTools:
    def __init__(self):
        self.rsrcmgr = PDFResourceManager()
        self.laparams = LAParams()
        self.device = PDFPageAggregator(self.rsrcmgr, laparams=self.laparams)
        self.interpreter = PDFPageInterpreter(self.rsrcmgr, self.device)
    

class Schedule(object):
    def __init__(self, pdf_doc = None):
        self.operations = []
        if pdf_doc is not None:
            self.pdf_doc = pdf_doc
    def __setDoc__(self, pdf_doc):
        if pdf_doc:
            self.pdf_doc = pdf_doc
        for i in self.operations:
            if not isinstance(i[1][0], PDFDocument):
                i[1].insert(0, self.pdf_doc)
            if i[1][0] is not self.pdf_doc:
                i[1][0] = self.pdf_doc
    def appendOp(self, op, args=[]):
        self.operations.append([op, args])
    def prelimOp(self, op, args=[]):
        self.operations.insert(0, [op, args])
    def execute(self, doc):
        self.__setDoc__(doc)
        for i in self.operations:
            i[0](*i[1])

def GFTPdfWrapper(pdfFilename,schedule, pdf_pwd=""):
    '''
        Open the pdf document, and apply the schedule
    '''
    #pdf file stuff
    fp = open(pdfFilename, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize(pdf_pwd)
    #execute schedule
    if doc.is_extractable:
        schedule.execute(doc)      #execute schedule
    #close file
    fp.close()

'''
meat
'''
        
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

class GFTArticleData:
    def __init__(self):
        self.guess_title = "" ;    #猜测的文章标题
        self.possible_titles = []
        self.author = [] ;         #监控而得到的针对性的研究员信息
        self.data_table = [] ;     #数据表的内容项
        self.figure = [] ;         #研报中引用到的图片
        self.content = "" ;        #研报中的所有正文文字
        self.lsStr = [] ;          #value为GFTPdfString
    def add_possible_title(self, str, height, width):
        value = height ** 2 + width
        self.possible_titles.append((str, value))
        self.possible_titles = sorted(self.possible_titles, key=lambda pair: pair[1], reverse=True)
        if len(self.possible_titles) > 5:
            del self.possible_titles[5]

def get_all_sub_class(lt_obj, class_type, lsRlt):
    '''
        lt_obj: parent obj
        class_type: sub class type
        lsRlt: out put list 
    '''
    if "__iter__" in dir(lt_obj) :
        for obj in lt_obj :
            if isinstance(obj , class_type) :
                lsRlt.append(obj) ;
            else :
                get_all_sub_class(obj , class_type , lsRlt) ;
                
def chg_pdf_coord(pdfobj,pgHeight):
    return (pdfobj.x0 , pgHeight - pdfobj.y1 , pdfobj.x1 , pgHeight - pdfobj.y0 ) ;

def pdf_object_sort(o1,o2):
    return o1.x0 + (5000-o1.y1) > o2.x0 + (5000-o2.y1)

''' 
muscle
'''     

def _gftParsePages(docObj, pmtools, parseMethod, args):
    '''
        iterate through docObj, call parseMethod for each page
        args: args for parse Method
    '''
    for i, page in enumerate(docObj.get_pages()):
        pmtools.interpreter.process_page(page)
        # receive the LTPage object for this page
        layout = pmtools.device.get_result()
        # layout is an LTPage object which may contain child objects like LTTextBox, LTFigure, LTImage, etc.
        parseMethod(layout, (i+1), **args)
        
def gftParsePage(docObj, pmtools, page_number, parseMethod, args):
    page = docObj.get_pages()[page_number]
    pmtools.interpreter.process_page(page)
    layout = pmtools.device.get_result()
    parseMethod(layout, (i+1), **args)

def _parse_lt_objs(lt_objs, page_number, resultData=None, parseTextMethod=None, \
                   parseImageMethod=None, parseLineMethod=None, onParseOver=None):
    '''
        analyse page object. 
        get article info such as title, author , figures.
    '''
    txtResult = []
    imgResult = []
    lineResult = []
    for lt_obj in lt_objs:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            #text
            if parseTextMethod is not None:
                parseTextMethod((lt_obj, lt_objs), txtResult)
        elif isinstance(lt_obj, LTImage):
            # an image
            if parseImageMethod is not None:
                imageResult = parseImageMethod((lt_obj, lt_objs), imgResult)
        elif isinstance(lt_obj, LTFigure):
            # LTFigure objects are containers for other LT* objects, so recurse through the children
            _parse_lt_objs(lt_obj, page_number, parseTextMethod, parseImageMethod, parseLineMethod)
            pass 
        elif isinstance(lt_obj, LTLine):
            # line obj
            if parseLineMethod is not None:
                lineResult = parseLineMethod((lt_obj, lt_objs), lineResult)
    if onParseOver is not None:
        onParseOver((lt_objs, page_number), [txtResult, imgResult, lineResult], resultData)

def _ana_textinfo(contextTube, resultList):
    ''' 
                  分析文本信息，拆解出标题和一整段的文字 
       contextTube : (lt_obj, lt_objs) in which lt_obj is the obj to parse, 
                                                lt_obj is the parent node/object of lt_obj 
       return : a list containing parsed GFTPdfStrings in lt_obj
    '''
    lt_obj = contextTube[0] 
    pg_height = contextTube[1].y1   # pg_height: page height
    h = resultList                          # h: a list to hold parsed strings.
    lsLTChar = [] 
    get_all_sub_class(lt_obj,LTChar,lsLTChar) 
    pct=0.5 
    lsLTChar.sort(pdf_object_sort) 
    for c in lsLTChar :
        if len(c.get_text()) == 0 :
            continue 
        key_found = False 
        (x0,y0,x1,y1) = chg_pdf_coord(c,pg_height)  #PDF的坐标轴是反向的，所以必须做一层转换
        if h :
            for o in h :
                rev = o.font_size * pct 
                if x0 >= (o.x1-rev*4) and x0 <= (o.x1 +rev*4) and \
                    y0 >= (o.y0-c.size/2) and y0 <= (o.y0 + c.size/2) \
                    and y1 >= (o.y1 - c.size/2) and y1 <= (o.y1 + c.size/2)\
                     and abs(c.size - o.font_size) <= max(c.size , o.font_size)*2.0/3.0 :
                    o.str = o.str + c.get_text() 
                    o.x0 = min(o.x0,x0) 
                    o.x1 = max(o.x1,x1) 
                    o.y0 = min(o.y0,y0) 
                    o.y1 = max(o.y1,y1) 
                    key_found = True 
                    break 
        if not key_found :
            curChar = GFTPdfString() 
            curChar.str = c.get_text() 
            curChar.font_name = c.fontname 
            curChar.font_size = c.size 
            curChar.x0 = x0 
            curChar.y0 = y0 
            curChar.x1 = x1 
            curChar.y1 = y1 
            h.append(curChar) 
    return h
   
def pageParseOver(contextTube, resultLists, articleData):
    '''
        called when a pages is parsed
        contextTube : (lt_objs, page_number)
        resultLists: [txtlist, imglist, linelist]
        articleData: used to save parsed data
    '''
    page_number = contextTube[1]
    page_text = resultLists[0]
    peAuthor = re.compile(r"(S\d{13})") 
    peTableChart = re.compile(ur"(^[图表]{1,}格{0,}\s*[\d一二三四五六七八九十]{1,}[:|：]*\s*\S*)") 
    peImage = re.compile(ur"([^表]附*图+表*[\s\t]*[\d一二三四五六七八九十]+[:|：]*\s*\S*)")
    peTable = re.compile(ur"([^图]附*表+格*[\s\t]*[\d一二三四五六七八九十]+[:|：]*\s*\S*)")
    for o in page_text :
        if o.str and len(o.str.strip()) > 0 :
            #print >>debug_file, "%s(x0=%d,y0=%d,w=%d,h=%d,pg=%d)%s"%(o.str,o.x0 , o.y0 , o.x1-o.x0 , o.y1-o.y0,page_number,os.linesep) 
            if page_number == 1 :
                #按照字体大小，来决定文章的标题
                articleData.add_possible_title(o.str.strip(), abs(o.y1 - o.y0), abs(o.x1 - o.x0))
                articleData.guess_title = articleData.possible_titles[0][0]
                lsAna = peAuthor.findall(o.str.strip()) 
                if lsAna :
                    for au in lsAna :
                        articleData.author.append(au) 
            lsChart = peTableChart.findall(o.str.strip()) 
            if lsChart :
                for ch in lsChart :
                    articleData.data_table.append(ch) 
                #if peTable.findall(o.str):
                #    print "table found at", page_number
                #    print "table name: ", o.str
            o.page_num = page_number 
            articleData.lsStr.append(o)
    if articleData.lsStr: 
        articleData.content = articleData.content + os.linesep.join([o.str for o in articleData.lsStr])
        articleData.lsStr = []

'''
   api
'''

def parsePDF(filename, handledata):
    '''
        filename: pdf file name 
        handedata: a function called after pdf is parsed, 
                   and a GFTArticleData object holding results will be passed to it,
                   i.e, handledata(article), where article is a GFTArticleData object
    '''
    article = GFTArticleData()
    parseGFTArticle = Schedule()
    pmtools = pdfMinerTools()
    parseGFTArticle.appendOp(_gftParsePages, [pmtools, _parse_lt_objs, {"parseTextMethod": _ana_textinfo, \
                                                                        "onParseOver": pageParseOver,     \
                                                                        "resultData": article             \
                                                                       }])
    #parseGFTArticle.appendOp()
    GFTPdfWrapper(filename, parseGFTArticle, pdf_pwd="")
    handledata(article)

def outPutArticle(article):
    print article.guess_title
    print "\t".join(article.author)
    if article.data_table:
        print "获取的内容： "
        for t in article.data_table:
            print t
    print article.content
           
if __name__ =="__main__":
    parsePDF(r'C:\test3.pdf',outPutArticle)
    