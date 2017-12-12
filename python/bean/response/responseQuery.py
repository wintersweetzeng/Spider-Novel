#-*- conding:UTF-8 -*-
__author__ = 'liudashuang'

class ResponseQuery:
    def __init__(self, img, title, url, author, novelType, lastUpdateChapter, lastUpdateTime):
        self.imageUrl = img
        self.title = title
        self.novelUrl = url
        self.author = author
        self.novelType = novelType
        self.lastUpdateChapter = lastUpdateChapter
        self.lastUpdateTime = lastUpdateTime        


