#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*- 
import requests
import re
read_file_name=input('please input the filename:')
write_file_name=input('please input the filename:')
pat ='所在类目</li>    <li class="info title">(.*?)</li></ul><div id="ElementId"></div>'
pattern = re.compile(pat)
def  getclassify (url):
     re_url='http://www.taozhenduan.com/lmcx/taobao_category.php'
     data ={'product_1':url}
     r=requests.post(re_url,data)
     h=r.text
     h=''.join(h)
     reslist = re.findall(pattern, h)
     return reslist
#下面开始读取所在的类目
file_open=open(read_file_name,encoding= 'utf8')#,encoding= 'utf8'
file_write=open(write_file_name,'w',encoding= 'utf8')
item_str_head='http://item.taobao.com/item.htm?id='
j=0
for each_item in file_open:
     each_item=(each_item.split('\n'))[0]
     try:
          url=item_str_head+each_item
          text=getclassify (url)
          for each in text:
               if each=='':
                    each='empty class'
               file_write.writelines(url+'|'+each.split('>')[0]+'\n')#
               print(each)
     except:
          print('error')
file_open.close()
file_write.close()
