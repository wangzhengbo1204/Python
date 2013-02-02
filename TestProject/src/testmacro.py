#-*- coding:utf-8 -*-
'''
Created on 2011-12-5

@author: GFTOwenWang
'''
import os


templet = '''<?xml version="1.0" encoding="UTF-8"?>
<DownloadingConfig xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="DownloadingConfig.xsd">
    <StartTime>00:00:01</StartTime>
    <EndTime>23:59:59</EndTime>
    <Frequency>5</Frequency>
    <DatabaseSetting>
        <DatabaseType>mssql</DatabaseType>
        <ConnectionString>DRIVER={SQL Server};SERVER=192.168.1.135;DATABASE=PG;UID=sa;PWD=123456</ConnectionString>
        <DatabaseName>PG</DatabaseName>
        <TableName>%s</TableName>
        %s
        <MonitorColumn>MTime</MonitorColumn>
        <Delimiter>chr(5)</Delimiter>
    </DatabaseSetting>
</DownloadingConfig>
'''

def test_macro():
    path = r'D:\GFT\FileServer\Resource\fileformat\FetchConfig\Genius MacConfig\3'
    path2 = r'D:\GFT\FileServer\Resource\fileformat\FetchConfig\Genius MacConfig\3old'
    list_filename = os.listdir(path)
    for filename in list_filename:
        if filename.startswith('1'):
            continue
        
        basename = os.path.splitext(filename)[0]
        file = open(os.path.join(path, filename),'rb')
        info = templet % (basename, file.read())
        file.close()
        print info
        
        file2 = open(os.path.join(path2, filename),'wb')
        file2.write(info)
        file2.close()
        
if __name__ == '__main__':
    test_macro()
    
    