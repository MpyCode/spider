# -*- coding:utf-8 -*-

# 爬虫总调main函数
import url_manager, html_downloader, html_parser,test_mkdir
import urllib2
import urllib
import os
import urlparse
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class SpiderMain(object):
    def __init__(self):
       
        self.urls = url_manager.UrlManager()
        
        self.downloader = html_downloader.HtmlDownload()
        
        self.parser = html_parser.HtmlParser()
        
        self.mkdirs=test_mkdir.MakeDir()

    def craw(self,root_url):
        url_list=['apache/hadoop/','apache/hbase/','apache/httpd/','apache/hive/','centos/7/cloud/']
        for url_base in url_list:
            fu_url=urlparse.urljoin(root_url,url_base)
            self.urls.addNewUrl(fu_url)
            while self.urls.hasNewUrl():
            
                    newUrl = self.urls.getNewUrl()
                    print('craw: %s'%newUrl)
                    if not os.path.exists('/home/mpy/download'+newUrl[25:]):#在这里添加指定文件夹，格式是：例如我的linux的用户是mpy，就像前面那样命名
                        os.makedirs('/home/mpy/download'+newUrl[25:])#在这里添加，规则如上
                    htmlCont = self.downloader.download(newUrl)
                    newUrls,newData = self.parser.parse(newUrl,htmlCont)
                    self.urls.addNewUrls(newUrls)
                    
                    if len(newData)!=0:
                        for dataurl in newData:
                        
                            str1=str(dataurl).split('/')[-1]
                            
                            #local=os.path.join('/home/mpy/codempy',dataurl[25:])
                            #os.chdir(local)
                            urllib.urlretrieve(dataurl,'/home/mpy/download/'+dataurl[25:])#在这里添加，规则如上，注意前两个最后没有'/',这里有'/'
                            
                            
                            

if __name__=="__main__":
    root_url = "http://mirrors.aliyun.com/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
