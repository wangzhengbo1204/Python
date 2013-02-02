'''
Created on 2011-12-8

@author: GFTOwenWang
'''
from __future__ import print_function
from win32com.client import Dispatch
import sys
import os


def test_func1():
    os.chdir(r'C:\Users\GFTOwenWang\Desktop\temp2')
    file_list = [r'C:\Users\GFTOwenWang\Desktop\temp2\sse_gz.htm']
    #file_list.extend(sys.argv[1:])
    if not file_list:
        file_list.extend(sys.stdin.read().split('\n'))
    try:
        iMsg = Dispatch('CDO.Message')
        for file in file_list:
            if not file:
                continue
            try:
                iMsg.CreateMHTMLBody('file:///' + file)
                iMsg.GetStream().SaveToFile(os.path.splitext(file)[0]+'.mht')
            except Exception as ex:
                raise
                #print 'Cannot save file: ' #% file
    finally:
        del iMsg
        
def test_func2():
    URL = r"http://www.sse.com.cn/sseportal/webapp/datapresent/SSEQueryBulletinOfTreasuryBillAct"
    FILEPATH = r"C:\Users\GFTOwenWang\Desktop\temp2\timgolden.me.uk.mht"
    
    message = Dispatch ("CDO.Message")
    message.CreateMHTMLBody (URL)
    stream = Dispatch (message.GetStream ())
    stream.SaveToFile (FILEPATH, 2)
    stream.Close ()
    
if __name__ == '__main__':
    test_func2()
    