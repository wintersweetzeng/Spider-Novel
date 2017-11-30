# -*- coding: UTF-8 -*-
__author__ = 'winter'
# 圣墟 parse


import os
from time import sleep
from parse.parseBase import ParseBase
from urlTools import UrlTools
from fileTools import FileTools
from logTools import Log

class ShenXuParse(ParseBase):
    def __init__(self, content):
        ParseBase.__init__(self, content)

    def setUrl(self, url):
        self.url = url

    def setLocalFolder(self, localFolder):
        self.localFolder = localFolder

    def downLoad(self, url):
        print("down load url ",url)
        Log.info('down load url '+url)
        urlTools = UrlTools(url)
        header, content = urlTools.getUrlContent()
        return content

    def writeToFile(self, link, no, title):
        url = self.url+link
        fileName = self.localFolder+ '/' + no + title+".n"
        if not os.path.exists(fileName): # chapter  not exist is need down
            # content is source page
            try:
                chapterPage = self.downLoad(url)
            except Exception, e:
                print e.message
                Log.error('error download url '+url+' error info '+e.message)
                sleep(1)
                chapterPage = self.downLoad(url)
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
                #第五百一十八
                # 海底宝藏
                noAndTitle = tmpTitleList[0].split(u'章')
                no = noAndTitle[0]+u'章'
                title = noAndTitle[1]
                self.writeToFile(link, no, title)