# -*- coding:UTF-8 -*-
__author__ = 'winter'
import json
from utils.fileTools import FileTools
from utils.logTools import  Log

from code import systemCode
from bean.response.responseNovel import ResponseNovel
from bean.response.responseChapter import ResponseChapter
from bean.response.responseChapterContent import ResponseChapterContent
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
                if '#' in content:
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

    def getChapterList(self, novelNo):
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+novelNo+u'/'+systemCode.oneNovelAllChaptersInfoFile)
        content = fileTools.readFile();
        chapters = []
        if content != "":
            contentList = content.split('\r\n')
            for index, raw in enumerate(contentList):
                if '#' in content:
                    chapterInfoList = raw.split(systemCode.fileContentSplit)
                    if len(chapterInfoList) == 2:
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
                 " chapterTitle [ %s ]  "%(novelNo, novelNo, chapterTitle))
        fileTools = FileTools(systemCode.baseFolder+u'/SourceUrlFile/'+novelNo+u'/'+chapterNo+chapterTitle+u'.n')
        content = fileTools.readFile();
        print(content)
        result = ResponseChapterContent(content)
        return ObjectJson.convert_to_dict(result)

