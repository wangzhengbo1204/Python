'''
Created on 2011-5-16

@author: GFTOwenWang
'''

import os
import MySQLdb


support_conn = MySQLdb.Connect(host="222.73.115.213", user="dataprogram", passwd="2.7182818", db="Data_Fundamental_Support", charset='utf8')

def get_itemname(item):
    strsql = "select OriIdtItemLabel from DCT_MEIOriIdtItems where OriIdtItem= '%s'"
    strsql = strsql % item 
    cursor = support_conn.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    
    return rs[0][0]

def get_list_itemnode():
    strsql = "select OriIdtItem, OriIdtItemAttribInstMapID from DCT_MEIOriIdtItemNodes where OriIdtItemAttribInstMapID is not null"
    cursor = support_conn.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    return rs

def list_attributetype_flag():
    strsql = "select RecordID from DCT_MEIOriIdtAttribTypes where SubItemFlag = 1"
    cursor = support_conn.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    list_itemflag = []
    if rs:
        for r in rs:
            list_itemflag.append(r[0])
            
    return list_itemflag

list_itemflag = list_attributetype_flag()

def get_attribute_type_value(instname):
    strsql = "select OriIdtAttribTypeID, OriIdtAttribTypeCodes from DCT_MEIOriIdtAttribInst where OriIdtAttribInstLabel = '%s'"
    strsql = strsql % instname
    cursor = support_conn.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    return rs[0]
    
def match_attributetype(mapid):
    dict_attrtype = {}
    
    strsql = "select OriIdtAttribInstIDs from DCT_MEIOriIdtAttribInstMap where RecordID = %s"
    strsql =strsql % mapid
    cursor = support_conn.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    
    if rs:
        instids = rs[0][0]
        list_instid = instids.replace('|',',').split(',')
        for instid in list_instid:
            type_values = get_attribute_type_value(instid)
            if type_values[0] in list_itemflag:
                dict_attrtype[type_values[0]] = type_values[1]
    else:
        instids = None
        
    return dict_attrtype

def get_attributetype(id):
    strsql = "select OriIdtAttribType, OriIdtAttribTypeLabel from DCT_MEIOriIdtAttribTypes where RecordID = %s"
    strsql = strsql % id
    cursor = support_conn.cursor()
    cursor.execute(strsql)
    rs = cursor.fetchall()
    return rs[0][0], rs[0][1]
    
def get_attributevalue(attributetype, values):
    strsql = "select OriIdtAttribCode,OriIdtAttribCodeLabel from DCT_MEIOriIdtAttribValues where OriIdtAttribType = '%s' and OriIdtAttribCode in %s"
    inst_values = repr(tuple(values))
    inst_values = inst_values.replace("u'","'").replace(",)",")")
    strsql = strsql % (attributetype, inst_values)
    cursor = support_conn.cursor()
    try:
        cursor.execute(strsql)
        rs = cursor.fetchall()
    except Exception as ex:
        print ex
    return rs
    
def generate(item, itemlabel, attrtype, attrtypelabel, code, codelabel):
    idt = u"%s%s%s" %(item, attrtype, code)
    idtlabel = u"%s-%s" %(itemlabel, codelabel)
    
    return idt, idtlabel
    
def main():
    list_item = []
    list_itemnode = get_list_itemnode()
    for itemnode in list_itemnode:
        item = itemnode[0]
        dict_attrtype = match_attributetype(itemnode[1])
        if dict_attrtype:
            itemlabel = get_itemname(item)
            for key, value in dict_attrtype.items():
                attributetype, typelabel = get_attributetype(key)
                values = value.split(',')
                list_attributevalues = get_attributevalue(attributetype, values)
                for attributevalues in list_attributevalues:
                    idt, idtlabel = generate(item, itemlabel, attributetype, typelabel, attributevalues[0], attributevalues[1])
                    tuple_item = (item, itemlabel, attributetype, typelabel, attributevalues[0], attributevalues[1], idt, idtlabel)
                    print ",".join(tuple_item)
                    list_item.append(tuple_item)
    
    file = open(r"d:\item.txt","wb")
    for item in list_item:
        str_item = ",".join(item)
        file.writelines("%s\r\n" % str_item)
    file.close()

main()