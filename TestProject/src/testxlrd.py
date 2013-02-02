#-*- coding:utf-8 -*-
'''
Created on 2011-12-17

@author: GFTOwenWang
'''
import xlrd
 
fname = r"D:\GFT\FileServer\TempParseFile\FL00002K6X.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name(u"三大报表")
except:
    print "no sheet in %s named Sheet1" % fname
    #return None
nrows = sh.nrows
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
 
cell_value = sh.cell_value(104,2)
print cell_value
 
row_list = []
for i in range(1,nrows):
    row_data = sh.row_values(i)
    row_list.append(row_data)

