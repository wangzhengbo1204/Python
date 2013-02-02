# -*- coding:utf-8 -*-
'''
Created on 2011-9-11

@author: GFTOwenWang
'''
from decimal import Decimal
import MySQLdb

parseconfig = '''<?xml version="1.0" encoding="UTF-8"?>
<ParsingConfig xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="D:GFTBackEndParserXsdParsingConfig.xsd">
    <MinPassedRatio>100</MinPassedRatio>
    <Encoding>utf-8</Encoding>
    <IsCreateCleanFile>true</IsCreateCleanFile>
    <TxtSetting>
        <Orientation>1</Orientation>
        <Delimiter>~^</Delimiter>
        <QuoteChar></QuoteChar>
        <Region>
            <StartLineNo>1</StartLineNo>
            <EndLine>
                <MaxBlankNumber>10</MaxBlankNumber>
            </EndLine>
        </Region>
        <GroupSetting>
            <KeySetting>
                <DataField DFid="594">
                    <ValuePattern>
                        <Location>
                            <AbsoluteExpression>1</AbsoluteExpression>
                        </Location>
                    </ValuePattern>
                </DataField>
                <DataField DFid="595">
                    <ValuePattern>
                        <Location>
                            <AbsoluteExpression>2</AbsoluteExpression>
                        </Location>
                        <DataFormatType>2</DataFormatType>
                        <DataFormat>YYYY-MM-DD</DataFormat>
                    </ValuePattern>
                </DataField>
            </KeySetting>
            <ValueSetting>
                <DataField DUid="393" DFid="596">
                    <ValuePattern>
                        <Location>
                            <AbsoluteExpression>3</AbsoluteExpression>
                        </Location>
                    </ValuePattern>
                </DataField>
            </ValueSetting>
        </GroupSetting>
    </TxtSetting>
</ParsingConfig>'''


def test1():
    #host = '222.73.115.213'
    host = '192.168.1.40'
    db_help = MySQLdb.connect(host=host, user='datatec', passwd='0.618', db='Data_Fundamental_Support', charset='utf8')
    strsql = "insert into DCP_ProviderParseConfigs(ProviderID,ParseConfigXML,EffectiveDate) values({0}, '{1}',now());"
#    i = 171
#    while True:
#        print i
#        strsql2 = strsql.format(i, parseconfig)
#        #strsql2 = MySQLdb.escape_string(strsql2)
#        cursor = db_help.cursor()
#        cursor.execute(strsql2)
#        cursor.execute("commit;")
#        cursor.close()
#        i += 1
#        if i > 194:
#            break
#        
    i = 91
    while True:
        print i
        strsql2 = strsql.format(i, parseconfig)
        #strsql2 = MySQLdb.escape_string(strsql2)
        cursor = db_help.cursor()
        cursor.execute(strsql2)
        cursor.execute("commit;")
        cursor.close()
        i += 1
        if i > 142:
            break
        
    
def is_duplicate_file(md5_code):
    strsql = '''select DocID from DCP_Doc where MD5Code = '{0}' AND DupFlag = 0 '''
    strsql = strsql.format(md5_code)
    cursor = db_help.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    cursor.close()
    db_help.close()
    if rs:
        return True
    else:
        return False
    
def insert_large_float():
    db_help = MySQLdb.connect(host='192.168.1.135', user='root', passwd='root', db='test', charset='utf8')
    value = 1029864647200.93
    value = Decimal(unicode(value))
    print 
    
#    strsql="insert into test.temp(a,b,c) value(1,2,%2f);" % value
#    cursor = db_help.cursor()
#    cursor.execute(strsql)
#    cursor.execute("commit;")
    
def insert():
    conn = MySQLdb.connect(host='192.168.1.135', user='root', passwd='root', db='Data_Fundamental_Support', charset='utf8')
    cursor = conn.cursor()
    for i in range(10):
        cursor.execute('start transaction')
        str_sql = "insert DCP_IDSeedDoc values();"
        cursor.execute(str_sql)
        str_sql = "SELECT LAST_INSERT_ID();"
        cursor.execute(str_sql)
        rs = cursor.fetchall()
        if rs:
            record_id = rs[0][0]
            print record_id
        cursor.execute('commit')
        
    cursor.close()
    
if __name__ == '__main__':
    test1()
