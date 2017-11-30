#-*- coding:UTF-8 -*-
__author__ = 'winter'

from time import ctime,sleep
import os, sys
from urlTools import UrlTools
from fileTools import FileTools
from logTools import  Log
from code import systemCode
# from parse.shenxuParse import ShenXuParse  python 3.5
from parse.shenxuParse import ShenXuParse
from novel.downloadnovelItem import DownLoadNovelItem

class SpiderMannager(object):
    def __init__(self):
        pass

    def manager(self):
        novels = []
        shenXuItem = DownLoadNovelItem(systemCode.baseUrl,systemCode.shenXuNovelUrl, systemCode.shenXuFileName, systemCode.shenXuLocalFolder);
        nineDayDrogen = DownLoadNovelItem(systemCode.baseUrl, systemCode.nineDayDrogenUrl, systemCode.nineDayDrogenFileName, systemCode.nineDayDrogenFolder)
        novels.append(shenXuItem)
        novels.append(nineDayDrogen)
        i = 1
        while True:
            for index, novel in enumerate(novels):
                print(u"download source page ")
                Log.info(u"download source page ")
                self.analysisNovelInfo(self.getNovel(novel), novel)
                print(u"parse source page ")
                Log.info(u"parse source page ")
                novelUrl = novel.baseUrl
                fileName = novel.fileName
                localFolder = novel.localFolder
                fileTools = FileTools(localFolder + "/" + fileName)
                content = fileTools.readFile()
                shenXuParse = ShenXuParse(content)
                shenXuParse.setUrl(novelUrl)
                shenXuParse.setLocalFolder(localFolder)
                shenXuParse.parse()
            print("no %s all over %s" %(i,ctime()))
            Log.info("no %s all over %s" %(i,ctime()))
            i = i + 1
            sleep(3600*12)


    def getNovel(self,novel):
        url = novel.novelUrl
        fileName = novel.fileName
        localFolder = novel.localFolder
        if not os.path.exists(localFolder):
            os.mkdir(localFolder)
        urlTools = UrlTools(url);
        header, content = urlTools.getUrlContent()
        fileTools = FileTools(localFolder+ u'/' +fileName);
        fileTools.writeNewFile(content)
        return content

    ##   name#url#author#imageurl#lashUpdateTime#lastUpdateChapter
    def analysisNovelInfo(self, content, novel):
        Log.info("analysisNovelInfo start")
        split= systemCode.fileContentSplit
        name = ''
        url = novel.novelUrl
        author = ''
        imageurl = ''
        lashUpdateTime = ''
        lastUpdateChapter = ''
        contentList = content.decode('utf-8').split('\r\n')
        for index, raw in enumerate(contentList):
            if '<h1>' in raw :
                name = raw.split('<h1>')[1].replace('</h1>', '')
            if '<p>作&nbsp;&nbsp;者：' in raw :
                author = raw.split('者：')[1].replace('</p>', '')
            if '<img alt' in raw :
                imageurl = systemCode.baseUrl+raw.split('src="')[1].split('" width')[0]
            if '<p>最后更新：' in raw :
                lashUpdateTime = raw.split('更新：')[1].replace('</p>', '')
            if ' <p>最新更新：' in raw :
                lastUpdateChapter = raw.split('">')[1].replace('</a></p>', '')
        novelinfo = name+ split +url+ split +author+ split \
                    +imageurl+ split +lashUpdateTime+ split +lastUpdateChapter
        Log.info(novelinfo)

        fileTools = FileTools(systemCode.baseFolder+ '/SourceUrlFile/'+systemCode.allNovelsNameInfoFile)
        allNovels = fileTools.readFile()
        tmpAllNovels = ''
        if allNovels != "":
            allNovelsList = allNovels.split('\r\n')
            for index,raw in enumerate(allNovelsList):
                if name in raw:
                    tmpAllNovels += novelinfo+'\r\n';
                else:
                    tmpAllNovels += raw+'\r\n';
        else:
            tmpAllNovels = novelinfo+'\r\n';
        fileTools1 = FileTools(systemCode.baseFolder+ '/SourceUrlFile/'+systemCode.allNovelsNameInfoFile)
        fileTools1.writeNewFile(tmpAllNovels)
        Log.info("analysisNovelInfo end")

