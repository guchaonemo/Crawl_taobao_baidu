#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-
import requests
import re
url='http://www.juanpi.com/click/?id=71821429'
url_Juanpi='http://www.juanpi.com'
useagernt={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'}
pat1='item.htm(.*?)"\r\n'
pattern1 = re.compile(pat1)
pat2='www.juanpi.com/click/(.*?)"'
pattern2 = re.compile(pat2)
#下面这个函数是为了获取淘宝宝贝id
def GetJuanpi(url):
    r=requests.get(url,headers=useagernt)
    h=r.content
    h=str(h, encoding = "utf-8")
    item=re.findall(pattern1, h)
    itemId=item[0].split('?')[1]
    return itemId
#下面这个函数为了获取卷皮网所有宝贝id
def GetJuanpiClick(url):
    r=requests.get(url,headers=useagernt)
    h=r.text
    relist=re.findall(pattern2, h)
    return relist
##http://www.taowola.com/tao.php?tao_up_id=78165
def ReadUrl(FileName):
    FileRead=open(FileName,'r',encoding= 'utf8')
    UrlList=FileRead.readlines()
    FileRead.close()
    List=[]
    for eachurl in UrlList:
        url=eachurl.split('\n')[0]
        List.append(url)
    return List
FileName=input('please input the name of the file:')
List=ReadUrl(FileName)
FileName='采集卷皮.txt'
FileWrite=open(FileName,'w',encoding= 'utf8')
for JuanPi in List:
    try:
        relist=GetJuanpiClick(JuanPi)
    except:
        print('ok finished!!!')
    for JuanPiId in relist:
        url='http://www.juanpi.com/click/'+JuanPiId
        try:
            h=GetJuanpi(url)
            FileWrite.writelines(h+'\n')
        except:
            print('this is not an taobao!!')
FileWrite.close()
