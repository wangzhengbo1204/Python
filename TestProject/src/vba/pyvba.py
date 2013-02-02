#-*- coding:utf-8 -*-
'''
Created on 2012-2-29

@author: GFTOwenWang
'''
import psutil
import win32com.client


def callvba():
    filename = ur"d:\a.xlsm"
    app = win32com.client.Dispatch("Excel.Application")
    app.DisplayAlerts = False
    app.ScreenUpdating = False
    workbook = app.Workbooks.Open(filename)
    app.ActiveWorkbook.Sheets(1).Cells.Clear()
    sh = app.ActiveWorkbook.Sheets(1)
    for i in range(1,30):
        sh.Cells(i, 1).Value = i
        sh.Cells(i, "B").Formula = "=mycontent(\"B" + str(i) + "\")"
        sh.Cells(i, "C").Formula = "=mycontent(\"C" + str(i) + "\")"
    
    for i in range(1,30):
        print sh.Cells(i,"A").Value, sh.Cells(i,"C").Value, sh.Cells(i,"C").Value
    workbook.Save
    app.DisplayAlerts = True
    app.ScreenUpdating = True
    
def call_wind():
    filename = ur"d:\temp\4wind2.xls"
    app = win32com.client.Dispatch("Excel.Application")
    app.DisplayAlerts = False
    app.ScreenUpdating = False
    workbook = app.Workbooks.Open(filename)
    workbook.Sheets(1).Cells(1,"B").Value = "Vie"
    workbook.Sheets(1).Cells.Select
    app.Selection.Copy()
    
    xlBook = app.Workbooks.Add()
    xlSheet1 = xlBook.Worksheets("sheet1")
    xlSheet1.Activate()
    xlSheet1.Cells.PasteSpecial(-4163)
    value = xlSheet1.Cells(5,2).Value
    print value
    xlBook.SaveAs(ur"d:\temp\4wind7.xls")
    app.DisplayAlerts = True
    app.ScreenUpdating = True
    xlBook.Close()
    app.Quit()
    
def test_process():
    pid = None
    for i in psutil.get_process_list():
        if i.name == "EXCEL.EXE":
            pid = i.pid
        print i.name, i.pid
    
    if pid:
        p = psutil.Process(pid)
        print p
        print "create excel.application"
        app = win32com.client.Dispatch("Excel.Application")
        #app.Workbooks.Open(ur"C:\Users\GFTOwenWang\Desktop\abc.xlsx")
        app.Workbooks("abc.xlsx").Sheets(1).Cells(20,2).Value=50
        app.Workbooks("abc.xlsx").Close(SaveChanges=True)
        #app.Quit()
        

    
if __name__ == "__main__":
    #callvba()
    #call_wind()
    test_process()