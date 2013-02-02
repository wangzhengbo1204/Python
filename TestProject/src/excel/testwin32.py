# -*- coding:utf-8 -*-
'''
Created on 2012-9-18

@author: GFTOwenWang
'''
import win32com
print dir(win32com)
from win32com.client import Dispatch



def func1():
    app = Dispatch("Excel.Application")
    workbook = app.Workbooks.Open(r"d:\gold.xlsx")
    r = workbook.Worksheets("Sheet2").Range("A1:A10000")
    r.Clear()
    workbook.Worksheets("Sheet2").Cells(1,"A").Value=10
    workbook.Worksheets("Sheet2").Cells(2,"A").Formula="=A1+1"
    print workbook.FullName
    
def func2():
    app = Dispatch("Excel.Application")
    workbook = app.Workbooks.Open(r"d:\gold.xlsx")
    r = workbook.Worksheets("Sheet2")
    print r.UsedRange.Rows.Count
    maxn = r.UsedRange.Rows.Count
    
    value = r.Range("A1:A%s" % maxn).Value
    print value
    
    for c in r.Range("B1:B%s" % maxn):
        print c.Value
        c.Value = 'w'
    

if __name__ == "__main__":
    func2()
    
