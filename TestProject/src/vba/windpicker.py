#-*- coding:utf-8 -*-
'''
Created on 2012-3-1

@author: GFTOwenWang
'''
import os
from datetime import datetime
import win32com.client


storedatapath=ur"d:\GFT\Datatech\windcpfdata"


def commands():
    list_comm = []
    command_file = ur"command.txt"
    file = open(command_file, "rb")
    for comm in file:
        if comm.strip():
            field_comm = comm.strip().split(",")
            if len(field_comm)==2:
                stockid = field_comm[0]
                reportdate = datetime.strptime(field_comm[1], "%Y-%m-%d")
                list_comm.append((stockid, reportdate))
                    
    return list_comm

def calculation(list_comm):
    filename = ur"d:\GFT\Datatech\windcpfdata.xls"
    app = win32com.client.Dispatch("Excel.Application")
    app.DisplayAlerts = False
    app.ScreenUpdating = False
    workbook = app.Workbooks.Open(filename)
    for comm in list_comm:
        stockid = comm[0].decode("gbk")
        print stockid, comm[1]
        workbook.Sheets(1).Cells(1,"C").Value = stockid
        workbook.Sheets(1).Cells(3,"C").Value = comm[1]
        c=1
        while True:
            f = workbook.Sheets(1).UsedRange.Find("Fetching...")
            if not f or c>10:
                print f
                break
            else:
                print c
                c = c+ 1
        workbook.Sheets(1).UsedRange.Select()
        app.Selection.Copy()
        
        xlBook = app.Workbooks.Add()
        xlSheet1 = xlBook.Worksheets("sheet1")
        xlSheet1.Activate()
        xlSheet1.Cells(1,1).PasteSpecial(12)
        corpname = xlSheet1.Cells(9,"C").Value
        filefullname = saveas_filename(corpname, comm[1])
        print filefullname
        xlBook.SaveAs(filefullname)
        xlBook.Close()
    app.DisplayAlerts = True
    app.ScreenUpdating = True
    app.Quit()

def saveas_filename(corpname, reportdate):
    list_filename = os.listdir(storedatapath)
    filename_template = u"WindCPF%s%s.xls"
    filename = filename_template % (corpname, reportdate.year)
    if filename in list_filename:
        num = 2
        filename_template = u"WindCPF%s%s_%s.xls"
        while True:
            filename = filename_template % (corpname, reportdate.year, num)
            if filename in list_filename:
                num += 1
            else:
                break
    
    filefullname = os.path.join(storedatapath, filename)
    
    return filefullname


if __name__ == "__main__":
    list_comm = commands()
    calculation(list_comm)
            
            
