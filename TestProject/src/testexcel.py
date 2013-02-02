#-*- coding:utf-8 -*-
'''
Created on 2012-2-23

@author: GFTOwenWang
'''
import win32com.client

filename = r'd:\a.xlsm'

xlApp = win32com.client.Dispatch('Excel.Application')
xlApp.visible = 0 # 此行设置打开的Excel表格为可见状态；忽略则Excel表格默认不可见
xlBook = xlApp.Workbooks.Open(filename)

content = r'excellent!' # 需要写入Excel单元格的内容（字符串类型）
rows = 60000 # 需要写入的行数（整数类型）

# ExecuteExcel4Macro函数的参数必须为字符串类型
# 在该字符串参数中，依次包含了“宏函数所在的Excel表格名称”+“宏函数的名称”+“宏函数的参数”
# 在宏函数的参数中，字符串参数content需要在两边分别再加上一个"，整型参数rows只需通过str转换为字符串即可
#strPara = xlBook.Name + '!CallWind("' + content + '", ' + str(rows) + ')'
#strPara = xlBook.Name + 'Cell2("' + content + '")'
strPara = xlBook.Name + '!Cell2("' + content + '")'
#strPara = xlBook.Name + '!Cell3()'
try:
    status = xlApp.ExecuteExcel4Macro(strPara)
    print status
except Exception as ex:
    print ex

xlBook.Close(SaveChanges=True) # 关闭Excel，并保存更改