# -*- coding:utf-8 -*-
'''
Created on 2011-10-24

@author: GFTOwenWang
'''
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice


def main():
    # Open a PDF file.
    fp = open('naacl06-shinyama.pdf', 'rb')
    # Create a PDF parser object associated with the file object.
    parser = PDFParser(fp)
    # Create a PDF document object that stores the document structure.
    doc = PDFDocument()
    # Connect the parser and document objects.
    parser.set_document(doc)
    doc.set_parser(parser)
    # Supply the password for initialization.
    # (If no password is set, give an empty string.)
    #doc.initialize(password)
    doc.initialize("")
    # Check if the document allows text extraction. If not, abort.
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    device = PDFDevice(rsrcmgr)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in doc.get_pages():
        interpreter.process_page(page)
        

def test1():
    #fp = open('naacl06-shinyama.pdf', 'rb')
    fp = open('FL00000M26.pdf', 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize("")
    
    # Get the outlines of the document.
    outlines = doc.get_outlines()
    for (level,title,dest,a,se) in outlines:
        print (level, title)
    
    
if __name__ == '__main__':
    #main()
    test1()
    