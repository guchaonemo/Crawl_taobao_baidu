#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-
import requests
import re
import HTMLParser
import simplejson
import time
import csv
from bs4 import BeautifulSoup
import xlwt
#url='http://queqiao.qingtaoke.com/?r=magpie/index&kw=&sort=sq&onlyToday=0&cr=1&sq=1&mcr=10&msq=12&dp=1&mdp=5&xdp=100&s=4.7&l=3&fs=1&fl=1&om=1&c=&page='
url='http://queqiao.qingtaoke.com/?r=magpie/index&kw=&sort=sq&onlyToday=0&cr=0&sq=0&mcr=0&msq=0&dp=0&mdp=-1&xdp=-1&s=0&l=1&fs=0&fl=0&om=1&c%5B0%'#5D=1&page=2'
def GetContent(urls):
    useagernt={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'}
    r=requests.post(urls,useagernt)
    text=r.text
    return text
def GetTaobaoUrl(htmls):
    soup = BeautifulSoup(htmls,'html.parser')
    urls=[]
    h=soup.find_all('li')
    for each_li_tag in h:
        soup = BeautifulSoup(str(each_li_tag))
        if soup.li.attrs.has_key('class'):
            divtag=soup.find_all('div')
            for each_div_tag in divtag:
                soup = BeautifulSoup(str(each_div_tag))
                if soup.div.attrs['class']==['title']:
                    urls.append( soup.a.attrs['href'])
    return urls
#h=GetTaobaoUrl(GetContent(url))
def WriteFile(url,Dnum):
    FileName = time.strftime('%Y-%m-%d',time.localtime(time.time()))+'_'+Dnum+'.txt'
    print FileName
    FileWrite=open(FileName,'w')
    for page_num in range(1,101):
        page_num=str(page_num)
        urls=url+'5D='+Dnum+'&page'+page_num
        print urls
        try:
            h=GetTaobaoUrl(GetContent(urls))
            for each_url in h:
                FileWrite.writelines(each_url+'\n')
        except:
            pass
    FileWrite.close()
for Dnum in range(1,3):
    try:
        WriteFile(url,str(Dnum))
    except:
        pass
        
    
