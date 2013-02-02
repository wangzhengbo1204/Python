#-*- coding:utf-8 -*-
'''
Created on 2012-2-24

@author: GFTOwenWang
'''
import win32com.client


def call_func1():
    xls_file = ur"D:\VBA\Callvba.xlsm"
    xl_app = win32com.client.Dispatch("Excel.Application")
    xl_wb = xl_app.Workbooks.Open(xls_file)
    result = xl_app.Run("MyDatetime")
    print result
    xl_wb.Close(SaveChanges=True)
    xl_app.Quit()
    del xl_app
    
def call_sub1():
    xls_file = ur"D:\VBA\Callvba.xlsm"
    xl_app = win32com.client.Dispatch("Excel.Application")
    xl_wb = xl_app.Workbooks.Open(xls_file)
    result = xl_app.Run("MyName")
    print result
    xl_wb.Close(SaveChanges=True)
    xl_app.Quit()
    del xl_app
    
def call_func1_param():
    xls_file = ur"D:\VBA\Callvba.xlsm"
    xl_app = win32com.client.Dispatch("Excel.Application")
    xl_wb = xl_app.Workbooks.Open(xls_file)
    result = xl_app.Run("MyDatetimeParam","sh")
    print result
    xl_wb.Close(SaveChanges=True)
    xl_app.Quit() 
    del xl_app
    
def call_sub1_param():
    xls_file = ur"D:\VBA\Callvba.xlsm"
    xl_app = win32com.client.Dispatch("Excel.Application")
    xl_wb = xl_app.Workbooks.Open(xls_file)
    result = xl_app.Run("MyNameParam","owen")
    print result
    xl_wb.Close(SaveChanges=True)
    xl_app.Quit()
    del xl_app
    
def call_sub2():
    xls_file = ur"D:\VBA\Callvba.xlsm"
    xl_app = win32com.client.Dispatch("Excel.Application")
    xl_wb = xl_app.Workbooks.Open(xls_file)
    strPara = xl_wb.Name + '!MyAge()'
    status = xl_app.ExecuteExcel4Macro(strPara)
    print status
    xl_wb.Close(SaveChanges=True)
    xl_app.Quit()
    del xl_app
    

if __name__ == '__main__':
    #call_func1()
    #call_sub1()
    call_func1_param()
    #call_sub1_param()
    pass
    