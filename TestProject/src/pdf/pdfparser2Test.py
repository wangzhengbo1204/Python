#-*- coding:utf-8 -*-
import sys, os, glob 
import GFTPdfParser
 
path = r"c:\Reports"
test_files = []
global fp
fp = None

def dumpStr(fp, str):
    #print str
    print >> fp, str, "%s" % (os.linesep)
    
def dumpArticle(article):
    global fp
    dumpStr(fp, article.guess_title)
    dumpStr(fp,"\t".join(article.author))
    if article.data_table:
        dumpStr(fp, "获取的内容： ")
        for t in article.data_table:
            dumpStr(fp, t)
    dumpStr(fp, article.content)
    
for path_i, subs, files in os.walk(path):
    for fn in glob.glob(path + os.sep + "*.pdf") :
        print fn
        test_files.append(fn)

for i in test_files:
    try:
        print "parsing ", i
        global fp
        filename = i + "_parsedInfo.txt"
        fp = open(filename, "w")
        GFTPdfParser.parsePDF(i, dumpArticle)
        fp.close()
    except Exception, e:
        print "error parsing", i
        print [j for j in sys.exc_info()]
print "done"