#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*- 
import requests
import re
import urllib3
pat1='sellerId:"(.*?)",'
pattern1 = re.compile(pat1)
pat2='"total":(.*?),"'
pattern2 = re.compile(pat2)
fileName=input('please input the name of the file:')
def GetTotalComments(url):
    r=requests.get(url)
    text=r.text
    text = ''.join(text)
    sellerId = ''.join(re.findall(pattern1, text))
    itemId=url[url.index('=')+1:]
    rateurl='http://rate.tmall.com/list_detail_rate.htm?itemId='+itemId+'&sellerId='+sellerId
    comment_r=requests.get(rateurl)
    text=comment_r.text
    text = ''.join(text)
    totalComment = ''.join(re.findall(pattern2, text))
    return totalComment
fileRead=open(fileName,'r')
url_list=fileRead.readlines()
fileRead.close()
fileWriteComment=open('comment.txt','w')
i=0
for url in url_list:
    try:
        url=url.split('\n')[0]
        comment=GetTotalComments(url)
        url_w=url+'|'+comment+'\n'
        fileWriteComment.writelines(url_w)
        i=i+1
        print(comment,i)
    except:
        print('error in total %d',i)
fileWriteComment.close()
    
 

            
