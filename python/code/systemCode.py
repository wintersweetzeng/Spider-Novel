# -*- coding: UTF-8 -*-
__author__ = 'winter'
import platform
baseUrl = u"http://www.bixia.org"

##    no#name#url#author#imageurl#lashUpdateTime#lastUpdateChapter
allNovelsNameInfoFile="novelsNameInfo.txt"
##   no#name
oneNovelAllChaptersInfoFile="chaptersInfo.txt"
fileContentSplit='#'


baseFolder = ''
host = ''
novelFolder = ''


system = platform.system()
print(u'this operate system is ',system)
if system is 'Windows':
    host = u'127.0.0.1'
    baseFolder =  u"H:/workspace/workspace-python/Spider-Novel/python"
elif system == "Linux":
    host = u'106.14.45.230'
    baseFolder = u"/root/novel/python"
else:
    print 'unknow system!'

novelsSourceDir = baseFolder+u'/'+u'SourceUrlFile'

downloadNovelsInfoFile = baseFolder+u'/config/downloadNovelsInfo.ini'

shenXuLocalFolder = ''
nineDayDrogenFolder = ''
#圣墟
shenXuNovelUrl = u'http://www.bixia.org/27_27047/'


#九天神龙诀
nineDayDrogenUrl = u'http://www.bixia.org/41_41384/'


responseMethodError = '{"code":1000, "msg":"unsupport GET method, please use POST"}'


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
