#-*- conding:UTF-8 -*-
__author__ = 'winter'

class ResponseChapter(object):
    chapterNo = ''
    chapterTitle = ''
    chapterSourceUrl = ''

    def __init__(self, chapterNo = u'', chapterTitle = u'', chapterSourceUrl =u''):
        self.chapterNo = chapterNo
        self.chapterTitle = chapterTitle
        self.chapterSourceUrl = chapterSourceUrl
