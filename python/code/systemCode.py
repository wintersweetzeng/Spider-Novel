# -*- coding: UTF-8 -*-
__author__ = 'winter'
import platform
baseUrl = u"http://www.bixia.org"
baseFolder = ''
host = ''
novelFolder = ''


system = platform.system()
print(u'this operate system is ',system)
if system is 'Windows':
    host = u'127.0.0.1'
    baseFolder =  u"E:/python"
elif system == "Linux":
    host = u'106.14.45.230'
    baseFolder = u"/root/novel/python"
else:
    print 'unknow system!'

shenXuLocalFolder = ''
nineDayDrogenFolder = ''
#圣墟
shenXuNovelUrl = u'http://www.bixia.org/27_27047/'
shenXuFileName = u"圣墟.txt"

chapterList = u"shenxuList.txt"


#九天神龙诀
nineDayDrogenUrl = u'http://www.bixia.org/41_41384/'
nineDayDrogenFileName = u'九天神龙诀.txt'


if system is 'Windows':
    shenXuLocalFolder = u"E:/python/SourceUrlFile/shenXu"
    nineDayDrogenFolder =u"E:/python/SourceUrlFile/nineDayDrogen"
    novelFolder = u"E:/python/SourceUrlFile"
elif system == "Linux":
    shenXuLocalFolder = u"/root/novel/python/SourceUrlFile/shenXu"
    nineDayDrogenFolder =u"/root/novel/python/SourceUrlFile/nineDayDrogen"
    novelFolder = u"/root/novel/python/SourceUrlFile"
else:
    print 'unknow system!'
