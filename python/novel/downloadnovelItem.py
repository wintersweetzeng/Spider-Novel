# -*- coding: UTF-8 -*-
__author__ = 'winter'

class DownLoadNovelItem(object):
    baseUrl = ''
    novelUrl = ''
    fileName = ''
    localFolder = ''
    def __init__(self,baseUrl, novelUrl, fileName, localFolder):
        self.baseUrl = baseUrl
        self.novelUrl = novelUrl
        self.fileName = fileName
        self.localFolder = localFolder

    def baseUrl(self):
        return self.baseUrl

    def novelUrl(self):
        return self.novelUrl

    def fileName(self):
        return self.fileName

    def localFolder(self):
        return self.localFolder
