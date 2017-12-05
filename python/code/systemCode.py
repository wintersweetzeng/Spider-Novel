# -*- coding: UTF-8 -*-
__author__ = 'winter'
import platform
baseUrl = u"http://www.bixia.org"

##    no#name#url#author#imageurl#lashUpdateTime#lastUpdateChapter
allNovelsNameInfoFile="novelsNameInfo.txt"
##   no#name#chapterSourceUrl
oneNovelAllChaptersInfoFile="chaptersInfo.txt"
fileContentSplit='#'
## chapterSourceUrl#titleName
oneNovelAllChaptersSourceInfo="chaptersSourceInfo.txt"



baseFolder = ''
host = ''
novelFolder = ''


system = platform.system()
print(u'this operate system is ',system)
if system is 'Windows':
    host = u'127.0.0.1'
    baseFolder =  u'H:/workspace/workspace-python/Spider-Novel/python'
elif system == "Linux":
    host = u'*.*.*.*'
    baseFolder = u'/root/xiujian/novel/Spider-Novel/python'
else:
    print 'unknow system!'

novelsSourceDir = baseFolder+u'/SourceUrlFile'

downloadNovelsInfoFile = baseFolder+u'/config/downloadNovelsInfo.ini'


##id#name#pwd#org
userInfoFile = baseFolder + u'/userInfo/userInfo.ini'
##userid#NovelNo#chapterNo
userReadNovelFile = baseFolder + u'/userInfo/userReadNovel.ini'

responseMethodError = '{"code":1000, "msg":"unsupport GET method, please use POST"}'
responseError = '{"code":1, "msg":"operate is failed"}'
responseSucc = '{"code":0, "msg":"success"}'

registryErrorOrg = '{"code":10, "msg":"org error"}'
registryErrorAlready = '{"code":11, "msg":"already registry error"}'
registryErrorNameOrPwd = '{"code":12, "msg":"name or password is null"}'


loginErrorNameOrPwdNull = '{"code":20, "msg":"name or password is null"}'
loginErrorNameOrPwd = '{"code":21, "msg":"name or password is error"}'
loginErrorNotRegistry = '{"code":22, "msg":"this name not registry"}'

# if system is 'Windows':
#     shenXuLocalFolder = u"E:/python/SourceUrlFile/shenXu"
#     nineDayDrogenFolder =u"E:/python/SourceUrlFile/nineDayDrogen"
#     novelFolder = u"E:/python/SourceUrlFile"
# elif system == "Linux":
#     shenXuLocalFolder = u"/root/novel/python/SourceUrlFile/shenXu"
#     nineDayDrogenFolder =u"/root/novel/python/SourceUrlFile/nineDayDrogen"
#     novelFolder = u"/root/novel/python/SourceUrlFile"
# else:
#     print 'unknow system!'
