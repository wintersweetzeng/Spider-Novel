# -*- coding: UTF-8 -*-
__author__ = 'winter'

from code import systemCode

class DownLoadNovelItem(object):
    __baseUrl = ''
    __novelUrl = ''
    __SourcefileName = ''
    __localFolder = ''
    __novelNo = ''
    def __init__(self,baseUrl, novelUrl):
        self.__baseUrl = baseUrl
        self.__novelUrl = novelUrl
        self.__SourcefileName = self.parseNovelNo()+u'.txt'
        self.__localFolder = systemCode.novelsSourceDir+'/'+self.parseNovelNo()
        self.__novelNo = self.parseNovelNo()

    def baseUrl(self):
        return self.__baseUrl

    def novelUrl(self):
        return self.__novelUrl

    def fileName(self):
        return self.__SourcefileName

    def localFolder(self):
        return self.__localFolder

    def novelNo(self):
        return  self.__novelNo

    ##http://www.bixia.org/27_27047/
    #27_27047
    def parseNovelNo(self):
        return self.novelUrl().split('org/')[1].replace('/', '')

