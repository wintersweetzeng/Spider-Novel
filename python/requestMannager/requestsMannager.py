# -*- coding:UTF-8 -*-
__author__ = 'winter'
import json, time, random
from utils.fileTools import FileTools
from utils.logTools import  Log
from utils.urlTools import UrlTools
from urllib2 import urlopen
from utils.htmlTools import BeautifulSoup

from code import systemCode
from bean.response.responseNovel import ResponseNovel
from bean.response.responseChapter import ResponseChapter
from bean.response.responseChapterContent import ResponseChapterContent
from bean.response.responseNovelChapterSource import ResponseNovelChapterSource
from bean.response.responseUser import ResponseUser
from bean.response.responseReadChapter import ResponseReadChapter
from bean.response.responseQuery import ResponseQuery
from utils.objectJson import ObjectJson

class RequestMannager(object):

    def __init__(self):
        pass

    def getNovels(self):
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+systemCode.allNovelsNameInfoFile)
        content = fileTools.readFile();
        novels = []
        if content != "":
            contentList = content.split('\r\n')
            for index, raw in enumerate(contentList):
                if '#' in raw:
                    novelInfoList = raw.split(systemCode.fileContentSplit)
                    if len(novelInfoList) == 7:
                        novelInfo = ResponseNovel(novelInfoList[0],novelInfoList[1],novelInfoList[2],
                    novelInfoList[3],novelInfoList[4],novelInfoList[5],novelInfoList[6])
                        novels.append(novelInfo)
                    else:
                        Log.error("getNovels novel  %s  len  is not 7"%(raw))
                else:
                    Log.error("getNovels content  %s is error"%(raw))
        else:
            Log.error("getNovels content  %s NULL")
        return ObjectJson.convert_to_dicts(novels)

    def queryNovels(self, novelName):
        html = urlopen("http://zhannei.baidu.com/cse/search?s=3677118700255927857&q="+novelName)
        bsObj=BeautifulSoup(html)
        queryResults=[]
        for link in bsObj.findAll(class_="result-item result-game-item"):
            imgUrl=''
            title=''
            url=''
            author=''
            novelType=''
            lastUpdateTime=''
            lastUpdateChapter=''
            for imglink in link.findAll(class_="result-game-item-pic-link-img"):
                if 'src' in imglink.attrs:
                    imgUrl=imglink.attrs['src']                    
            for titlelink in link.findAll(class_="result-game-item-title-link"):
                if 'href' in titlelink.attrs:
                    url = titlelink.attrs['href']
                if 'title' in titlelink.attrs:
                    title=titlelink.attrs['title'].replace(' ', '').replace('\n', '')
            for lastupdatechapter in link.findAll(class_="result-game-item-info-tag-item"):
                if 'href' in titlelink.attrs:
                    lastchapter=lastupdatechapter.attrs['href']
            for novelinfo in link.findAll(class_="result-game-item-info"):
                author = novelinfo.findAll("p")[0].findAll("span")[1].get_text().replace(' ','').replace('\n', '')
                novelType = novelinfo.findAll("p")[1].findAll("span")[1].get_text()
                lastUpdateChapter = novelinfo.findAll("p")[2].findAll("span")[1].get_text()
                lastUpdateTime =  novelinfo.findAll("p")[3].findAll("a")[0].get_text()

            #novel=ResponseQuery(imgUrl, title,lastchapter)
            novel = ResponseQuery(imgUrl, title, url, author, novelType, lastUpdateChapter, lastUpdateTime)
            queryResults.append(novel)
        obj_arr=[]
        for obj in queryResults:
            dict={}
            dict.update(obj.__dict__)
            obj_arr.append(dict)
        return obj_arr

    def getChapterList(self, novelNo):
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+novelNo+u'/'+systemCode.oneNovelAllChaptersInfoFile)
        content = fileTools.readFile();
        chapters = []
        if content != "":
            contentList = content.split('\r\n')
            for index, raw in enumerate(contentList):
                if '#' in raw:
                    chapterInfoList = raw.split(systemCode.fileContentSplit)
                    if len(chapterInfoList) == 3:
                        chapterInfo = ResponseChapter(chapterInfoList[0],chapterInfoList[1],chapterInfoList[2])
                        chapters.append(chapterInfo)
                    elif len(chapterInfoList) == 2:
                        chapterInfo = ResponseChapter(chapterInfoList[0],chapterInfoList[1])
                        chapters.append(chapterInfo)

                    else:
                        Log.error("getChapterList novel  %s  len  is not 2"%(raw))
                else:
                    Log.error("getChapterList content  %s is error"%(raw))
        else:
            Log.error("getChapterList content  %s NULL")
        # Log.info("getNovels result "+chapters)
        return ObjectJson.convert_to_dicts(chapters)

    def getChapter(self, novelNo, chapterNo, chapterTitle):
        Log.info("getChapter novelNo [ %s ] chapterNo [ %s ] "
                 " chapterTitle [ %s ]  "%(novelNo, chapterNo, chapterTitle))
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+novelNo+u'/'+chapterNo+chapterTitle+u'.n')
        content = fileTools.readFile();
        result = ResponseChapterContent(content)
        return ObjectJson.convert_to_dict(result)


    def addOneNovel(self, novelNo):
        ok = False
        Log.info("addOneNovel novelNo [ %s ] "%(novelNo))
        url = systemCode.baseUrl+u'/'+novelNo+'/'
        urlTools = UrlTools(url)
        header, content = urlTools.getUrlContent()
        if '笔下文学' in content:
            fileTools = FileTools(systemCode.downloadNovelsInfoFile)
            content = fileTools.readFile()
            if novelNo not in content:
                fileTools = FileTools(systemCode.downloadNovelsInfoFile)
                fileTools.fileWriteAppend(novelNo+u'\r\n');
            Log.info("addOneNovel novelNo [ %s ] success "%(novelNo))
            ok = True
        else:
            Log.info("addOneNovel novelNo [ %s ] failed  maybe not 笔下文学 or novelNo is error"%(novelNo))
        return ok

    def getChapterSourceList(self, novelNo):
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+novelNo+u'/'+systemCode.oneNovelAllChaptersSourceInfo)
        content = fileTools.readFile();
        responseNovelChapterSources = []
        if content != "":
            contentList = content.split('\r\n')
            for index, raw in enumerate(contentList):
                if '#' in raw:
                    chapterInfoList = raw.split(systemCode.fileContentSplit)
                    if len(chapterInfoList) == 2:
                        chapterSourceInfo = ResponseNovelChapterSource(chapterInfoList[0],chapterInfoList[1])
                        responseNovelChapterSources.append(chapterSourceInfo)
                    else:
                        Log.error("getChapterSourceList novel  %s  len  is not 2"%(raw))
                else:
                    Log.error("getChapterSourceList content  %s is error"%(raw))
        else:
            Log.error("getChapterSourceList content  %s NULL")
        # Log.info("getNovels result "+chapters)
        return ObjectJson.convert_to_dicts(responseNovelChapterSources)

    ## id#name#pwd#org
    def registry(self, username, password, org):
        if org != 'Super':
            return systemCode.registryErrorOrg
        elif username == '' or password == '':
            return systemCode.registryErrorNameOrPwd
        else:
            fileTools = FileTools(systemCode.userInfoFile)
            allUser = fileTools.readFile()
            if username in allUser:
                return systemCode.registryErrorAlready
            else:
                split = systemCode.fileContentSplit
                millis = int(round(time.time()*100000))
                rand = random.randint(1, 1000)
                id = millis + rand
                user = str(id) + split + username +split + password + split + org+u'\r\n'
                fileTools = FileTools(systemCode.userInfoFile)
                fileTools.fileWriteAppend(user)
                user = ResponseUser(id, username, password, org)
                return ObjectJson.convert_to_dict(user)


    def login(self, username, password):
        if username == '' or password == '':
            return systemCode.loginErrorNameOrPwdNull
        else:
            fileTools = FileTools(systemCode.userInfoFile)
            allUser = fileTools.readFile()
            if username not in allUser:
                return systemCode.loginErrorNotRegistry
            else:
                userList = allUser.split(u'\r\n')
                for index, user in enumerate(userList):
                    if username in user and password in user:
                        id = user.split(systemCode.fileContentSplit)[0]
                        return '{"code":0, "msg":"success", "id":"'+str(id)+'"}'

            return systemCode.loginErrorNameOrPwd

    def userGetChapter(self, novelNo, chapterNo, chapterTitle, id):
        Log.info("userGetChapter novelNo [ %s ] chapterNo [ %s ] "
                 " chapterTitle [ %s ]  user id [%s]"%(novelNo, chapterNo, chapterTitle, id))
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+novelNo+u'/'+chapterNo+chapterTitle+u'.n')
        content = fileTools.readFile();

        split = systemCode.fileContentSplit
        userReadInfo = id + split + novelNo + split + chapterNo + split +chapterTitle
        fileTools = FileTools(systemCode.userReadNovelFile)
        readInfo = fileTools.readFile()
        if userReadInfo not in readInfo:
            fileTools = FileTools(systemCode.userReadNovelFile)
            fileTools.fileWriteAppend(userReadInfo)
        result = ResponseChapterContent(content)
        return ObjectJson.convert_to_dict(result)

    def queryUserReadChapter(self, novelNo,  id):
        Log.info("userGetChapter novelNo [ %s ]   user id [%s]"%(novelNo, id))
        fileTools = FileTools(systemCode.userReadNovelFile)
        readInfo = fileTools.readFile();
        split = systemCode.fileContentSplit
        list = readInfo.split('\r\n')
        result = []
        for index, raw in enumerate(list):
            tmp = raw.split(split)
            if len(tmp) == 4:
                id = tmp[0]
                novelNo = tmp[1]
                chapterNo = tmp[2]
                chapterTitle = tmp[3]
                if id == id and novelNo == novelNo:
                    Log.info("[ %s ] read [%s]"%(id, novelNo))
                    read = ResponseReadChapter(id, novelNo, chapterNo, chapterTitle)
                    result.append(read)
                else:
                    Log.info("[ %s ] not read [%s]"%(id, novelNo))
            else:
                Log.error("[ %s ] len is not 4 is [%s]"%(raw, str(len(tmp))))

        return ObjectJson.convert_to_dicts(result)
