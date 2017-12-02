#-*- conding:UTF-8 -*-
__author__ = 'winter'

class ResponseNovel(object):
    #no#name#url#author#imageurl#lashUpdateTime#lastUpdateChapter
    no = ''
    name = ''
    url = ''
    author = ''
    imageurl = ''
    lashUpdateTime = ''
    lastUpdateChapter = ''
    def __init__(self,no,name,url,author,imageurl,lashUpdateTime,lastUpdateChapter):
        self.no = str(no.encode('utf-8'))
        self.name = str(name.encode('utf-8'))
        self.url = str(url.encode('utf-8'))
        self.author = str(author.encode('utf-8'))
        self.imageurl = str(imageurl.encode('utf-8'))
        self.lashUpdateTime = str(lashUpdateTime.encode('utf-8'))
        self.lastUpdateChapter = str(lastUpdateChapter.encode('utf-8'))
