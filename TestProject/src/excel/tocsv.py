'''
Created on 2012-10-12

@author: GFTOwenWang
'''
import xlrd
import csv
from datetime import datetime
from gftdata.share.utility.date import getdatebyint

def csv_from_excel():
    wb = xlrd.open_workbook(ur'D:\temp\ReHis000001.xls')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(ur'D:\temp\ReHis000001.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_NONE)
    
    for rownum in xrange(sh.nrows):
        row=list(sh.row_values(rownum))
        if rownum>0 and sh.row_values(rownum)[1]:
            try:
                row[1] =  datetime.strftime(getdatebyint(sh.row_values(rownum)[1]),"%Y-%m-%d")
            except Exception as ex:
                print rownum
                print ex
        wr.writerow(row)
    
    your_csv_file.close()
    
csv_from_excel()
