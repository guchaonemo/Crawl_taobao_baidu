#-*-coding:utf-8-*-

import time
import urllib2, os.path as osp
import urllib
import sys  
import re   
import requests
import HTMLParser
from bs4 import BeautifulSoup  

# 采集速度控制，单位秒
sleep = 5
# 网页基础地址
# 设置提交的header头
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# 下载html文件
def getHtml(url):
    print "GET:",url
    html=""
    try:
        req = urllib2.Request(url=url,headers=headers)
        response = urllib2.urlopen(req,timeout=5)
        html=response.read()
    except urllib2.URLError as e:
      if hasattr(e, 'code'):
        print 'Error code:',e.code
      elif hasattr(e, 'reason'):
        print 'Reason:',e.reason
    finally:
        if response:
            response.close()
    return html
def GetSearchUrl(keyword):
        keyword=urllib.quote(keyword)
        baseurl="http://www.baidu.com/s?wd="
        url=baseurl+keyword
        return url
#获取百度搜索结果 
def GetResultContent(html):
    soup = BeautifulSoup(html,'html.parser')
    tags_div = soup.find_all('div')
    result=[]
    for tag_div in tags_div:
        soup = BeautifulSoup(str(tag_div))
        #下面是为了获取每一条搜索结果里面的链接
        if soup.div.attrs.has_key('class') and soup.div.attrs.has_key('data-click') and soup.div.attrs.has_key('id'):
            h=soup.div
            soup_div = BeautifulSoup(str(h),'html.parser')
            SearchResultUrl=GetSearchResultUrl(soup_div)
            result.append(SearchResultUrl)
    return result
def GetSearchResultUrl(soup_div):
    if soup_div.a.attrs.has_key('href'):
        a=soup_div.a.attrs['href']
        return a
key=raw_input('input key word:')
def GetAllSearchResult(key):
    next_page = GetSearchUrl(key)
    i=0
    FileName = time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.txt'
    FileWrite=open(FileName,'w')
    while i<5:
        try:
            html=getHtml(next_page)
            a=[]
            a=GetResultContent(html)
            soup = BeautifulSoup(html,'html.parser')
            if i==0:
                next_page='http://www.baidu.com'+soup('a',{'href':True,'class':'n'})[0]['href']
            else:
                next_page='http://www.baidu.com'+soup('a',{'href':True,'class':'n'})[1]['href']
            i=i+1
            for each_url in a:
                FileWrite.writelines(each_url+'\n')
        except:
            print 'error'
    print 'Finished!!!'
    FileWrite.close()
    return FileName
def GetChatUrl(url):
    html=getHtml(url)
    results=re.findall("(?isu)(http\://url.cn[a-zA-Z0-9\.\?/&\=\:]+)",html)
    return results
def originalURLs(baiduURLs):
    originalurls=[]
    for tmpurl in baiduURLs:
        try:
            urls = requests.get(tmpurl).url
            originalurls.append(urls)
        except:
            pass
    return originalurls


#获取百度搜索结果链接的链接
def ReadBaiduUrls(FileName):
    ReadBaiduUrls=[]
    BaiduUrls=[]
    FileWrite=open(FileName,'rb')
    for each in FileWrite:
        each=each.split('\n')
        ReadBaiduUrls.append(each[0])
    FileWrite.close()
    for each in ReadBaiduUrls:
        each=each.split('\r')
        BaiduUrls.append(each[0])
    return BaiduUrls
def GetInformation(originalurls):
    FileName =time.strftime('%Y-%m-%d',time.localtime(time.time()))+'bai_du.txt'
    FileWrite=open(FileName,'w')
    for each in originalurls:
        try:
            urls=GetChatUrl(each)
            urls=list(set(urls))
            for each_url in urls:
                print each_url
                FileWrite.writelines(each_url+'\n')
        except:
            pass
    FileWrite.close()
FileName=GetAllSearchResult(key)
Baiduurls=(ReadBaiduUrls(FileName))
GetInformation(Baiduurls)
url='http://www.meipai.com/media/418923454'
#GetChatUrl(url)


