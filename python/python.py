# -*- coding: UTF-8 -*-
import sys

from flask import Flask, request,render_template
import os, sys
from time import ctime,sleep

from urlTools import UrlTools
from fileTools import FileTools
from logTools import  Log

# from parse.shenxuParse import ShenXuParse  python 3.5
from parse.shenxuParse import ShenXuParse
from novel.downloadnovelItem import DownLoadNovelItem
from code import systemCode

import threading

app = Flask(__name__)

reload(sys)
sys.setdefaultencoding( "utf-8" )

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template(systemCode.baseFolder+u'/index.html',title = 'Home')
    # return systemCode.baseFolder+u'/index.html'  http://www.jb51.net/article/64452.htm

def manager():
    novels = []
    shenXuItem = DownLoadNovelItem(systemCode.baseUrl,systemCode.shenXuNovelUrl, systemCode.shenXuFileName, systemCode.shenXuLocalFolder);
    nineDayDrogen = DownLoadNovelItem(systemCode.baseUrl, systemCode.nineDayDrogenUrl, systemCode.nineDayDrogenFileName, systemCode.nineDayDrogenFolder)
    # novels.append(shenXuItem)
    novels.append(nineDayDrogen)
    i = 1
    while True:
        for index, novel in enumerate(novels):
            print(u"download source page ")
            Log.info(u"download source page ")
            getNovel(novel)
            print(u"parse source page ")
            Log.info(u"parse source page ")
            # novelUrl = u'http://www.bixia.org'
            # fileName = u"圣墟.txt"
            # novelUrl = systemCode.baseUrl
            # fileName = systemCode.shenXuFileName
            # localFolder = systemCode.shenXuLocalFolder
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

def getNovel(novel):
    # url = u"http://www.bixia.org/27_27047/"
    # fileName = u"圣墟.txt";

    # url = systemCode.shenXuNovelUrl
    # fileName = systemCode.shenXuFileName
    # localFolder = systemCode.shenXuLocalFolder
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

@app.route('/LoveNovel/getShenXuAllChapter', methods=['POST', 'GET'])
def getShenXuAllChapter():
    shenXuDir = systemCode.shenXuLocalFolder
    list = os.listdir(shenXuDir)
    result=[]
    for index, file in enumerate(list):
        if '.n' in file:
            result.append(file)
    # list to string
    resultStr = ''.join(result)
    return resultStr

@app.route('/LoveNovel/getShenXuAllNovel', methods=['POST', 'GET'])
def getShenXuAllNovel():
    novelDir = systemCode.novelFolder
    list = os.listdir(novelDir)
    result=[]
    for index, file in enumerate(list):
        result.append(file)
    # list to string
    resultStr = ''.join(result)
    return resultStr

@app.route('/LoveNovel/getShenXuChapter', methods=['POST', 'GET'])
def getChapter():
    if request.method == 'GET':
        file = request.args.get('no', type=str, default=None)
        print('getShenXuChapter file', file)
        if file is None:
            file = u'第一章 沙漠中的彼岸花'+u'.n'
        # shenXuDir=u"E:/python/SourceUrlFile/圣墟"
        shenXuDir = systemCode.shenXuLocalFolder
        fileTools = FileTools(shenXuDir + u'/' + file)
        content = fileTools.readFile()
        return content
    else:
        return ''


updateNovelThreads = []
updateThread = threading.Thread(target=manager,args=())
updateNovelThreads.append(updateThread)


@app.route('/LoveNovel/updateNovel', methods=['POST', 'GET'])
def updateNovel():
    for thread in updateNovelThreads:
        thread.setDaemon(True)
        thread.start()
    return "OK"

if __name__ == '__main__':
    # for thread in updateNovelThreads:
    #     thread.setDaemon(True)
    #     thread.start()
    app.run(host=systemCode.host, port='5000', debug=False)

