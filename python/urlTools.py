# -*- coding: UTF-8 -*-
__author__ = 'winter'

# from  urllib import request  python 3.5
import urllib
print("urlTools")
class UrlTools:
    url = "http://www.baidu.com"
    def __init__(self):
        pass
    def __init__(self, url):
        self.url = url
    def getUrlContent(self):
        page = urllib.urlopen(self.url)
        data = page.read()
        # header = page.getheaders()
        header = "fake header"
            #print('status:',page.status,page.reason)
            #for k,v in page.getheaders():
                #print('%s : %s'%(k,v))
        #print('data:',data.decode('utf-8'))
        return header,data

# url = UrlTools("http://www.baidu.com");
# print(url.getUrlContent())



