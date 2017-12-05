# -*- coding: UTF-8 -*-
__author__ = 'winter'
# 圣墟 parse


import os
from time import sleep

from parse.parseBase import ParseBase
from utils.urlTools import UrlTools
from utils.fileTools import FileTools
from utils.logTools import Log
from code import systemCode


class BiXiaWenXueParse(ParseBase):
    def __init__(self, content):
        ParseBase.__init__(self, content)

    def setUrl(self, url):
        self.url = url

    def setLocalFolder(self, localFolder):
        self.localFolder = localFolder

    def setNovelNo(self, novelNo):
        self.novelNo = novelNo

    def downLoad(self, url):
        print("down load url ",url)
        Log.info('down load url '+url)
        urlTools = UrlTools(url)
        header, content = urlTools.getUrlContent()
        return content

    def writeToFile(self, link='', no='', title=''):
        url = self.url+link
        url = url.replace('//', '/')
        url = url.replace(':/', '://')
        fileName = self.localFolder+ '/' + no + title+".n"
        if not os.path.exists(fileName): # chapter  not exist is need down
            # content is source page
            try:
                chapterPage = self.downLoad(url)
            except Exception, e:
                print e.message
                Log.error('one error download url '+url+' error info '+e.message)
                sleep(30)
                try:
                    chapterPage = self.downLoad(url)
                except Exception, e:
                    sleep(120)
                    Log.error('two error download url '+url+' error info '+e.message)
                    chapterPage = self.downLoad(url)
            self.analysisChapterInfo(no, title, url)
            fileTools = FileTools(fileName)
            # fileTools.writeNewFile(chapterPage) # chapter content contains others info
            #replace
            chapterPageList = chapterPage.decode('utf-8').split('\r\n') # analysis the chapter content
            for index, raw in enumerate(chapterPageList):
                if '<br/>' in raw:
                    # fileTools.writeNewFile(bytes(raw, encoding='utf-8')) python 3.5
                    raw = raw.decode('utf-8')
                    fileTools.writeNewFile(bytes(str(raw)))
        else:
            print(fileName, "is already download!")
            Log.info(fileName + "is already download!")

    def parse(self):
        contentList = self.content.decode('utf-8').split('\r\n')
        for index, raw in enumerate(contentList):
            if '<dd>' in raw  and u'月票'  not in raw and u'推迟' not in raw and u'第' in raw:
                raw = raw.replace(u'掌', u'章')  #修改错别字
                raw = raw.replace(u':', u' ')  #修改错别字
                raw = raw.replace(u'?', u'')  #修改错别字
                ##<dd> <a style="" href="/27_27047/2325047.html">第七百七十五章 专打老天才</a></dd>   to
                #/27_27047/2325047.html">第七百七十五章 专打老天才</a></dd>
                chapterList = raw.split('href="');
                ##/27_27047/2325047.html">第七百七十五章 专打老天才</a></dd>      to
                #/27_27047/2325169.html
                # 第七百七十六章 都送上路</a></dd>
                tmpList = chapterList[1].split('">')
                link = tmpList[0]
                ##第七百七十六章 都送上路</a></dd>     to
                #第七百七十六章 都送上路
                tmpTitleList = tmpList[1].split('</a>')
                ##第七百七十六章 都送上路
                #第七百七十六章都送上路
                nospaceString = tmpTitleList[0].replace(' ','')
                ##第七百七十六章都送上路
                #第五百一十八
                # 海底宝藏
                noAndTitle = nospaceString.split(u'章')
                no = noAndTitle[0]+u'章'
                title = noAndTitle[1]
                self.writeToFile(link, no, title)
            elif '<dd>' in raw  and u'月票'  not in raw and u'推迟' not in raw:
                raw = raw.replace(u'?', u'')  #修改错别字
                raw = raw.replace(u':', u' ')  #修改错别字
                ##<dd> <a style="" href="/167_167729/8536701.html">1 入职</a></dd>   to
                #/27_27047/2325047.html">1 入职</a></dd>
                chapterList = raw.split('href="');
                ##/27_27047/2325047.html">1 入职</a></dd>      to
                #/27_27047/2325169.html
                #1 入职</a></dd>
                tmpList = chapterList[1].split('">')
                link = tmpList[0]
                ##1 入职</a></dd>     to
                #1 入职
                tmpTitleList = tmpList[1].split('</a>')
                ##1 入职
                #1
                #入职
                noAndTitle = tmpTitleList[0].split(' ')
                if len(noAndTitle) == 2:
                    no = noAndTitle[0]
                    title = noAndTitle[1]
                    self.writeToFile(link, no, title)
                else:
                    Log.error("parse chapter[ %s ]no  title except is 2 !"%(raw))
            else:
                Log.error(" parse chapter info is unsupport !")
            self.annalysisChapterSourceInfo(raw);
    ##   no#name#chapterSourceUrl
    def analysisChapterInfo(self, no='', title='', chapterSourceUrl=''):
        Log.info("analysisChapterInfo start")
        fileTools = FileTools(self.localFolder+'/'+systemCode.oneNovelAllChaptersInfoFile)
        split = systemCode.fileContentSplit
        info = no + split + title +split+chapterSourceUrl+'\r\n'
        fileTools.fileWriteAppend(info)
        Log.info("analysisChapterInfo end")
    ## chapterSourceUrl#titleName
    def annalysisChapterSourceInfo(self, raw):
        Log.info("annalysisChapterSourceInfo  [%s] "%(raw))
        ##<dd> <a style="" href="/167_167729/8536723.html">23 樱花的忍者</a></dd>
        if '<dd> <a' in raw:
            ####<dd> <a style="" href="/167_167729/8536723.html">23 樱花的忍者</a></dd>
            #<dd> <a style=""
            #/167_167729/8536723.html">23 樱花的忍者</a></dd>
            tmp = raw.split('href="')
            ##/167_167729/8536723.html">23 樱花的忍者</a></dd>
            #/167_167729/8536723.html
            # 23 樱花的忍者</a></dd>
            tmp1 = tmp[1].split('">')
            link = tmp1[0]
            titleName = tmp1[1].replace('</a></dd>', '')
            chapterSourceUrl = self.url+link
            chapterSourceUrl = chapterSourceUrl.replace('//', '/')
            chapterSourceUrl = chapterSourceUrl.replace(':/', '://')
            chapterSourceInfo = chapterSourceUrl + systemCode.fileContentSplit+titleName

            Log.info(chapterSourceInfo)

            fileTools = FileTools(systemCode.baseFolder+ u'/SourceUrlFile/'+
                                  self.novelNo + u'/'+systemCode.oneNovelAllChaptersSourceInfo)
            allChaptersSource = fileTools.readFile()
            # if allNovels != "":
            if chapterSourceInfo not in allChaptersSource:
                fileTools1 = FileTools(systemCode.baseFolder+ u'/SourceUrlFile/'+
                                  self.novelNo + u'/'+systemCode.oneNovelAllChaptersSourceInfo)
                fileTools1.fileWriteAppend(chapterSourceInfo)
            else:
                Log.info("annalysisChapterSourceInfo [%s]  is already exist!"%(chapterSourceInfo))
