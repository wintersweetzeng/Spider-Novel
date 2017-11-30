#-*- conding:UTF-8 -*-
__author__ = 'winter'

from fileTools import FileTools
from code import systemCode
logFileName = systemCode.baseFolder+u'/'+u'novel.log'
class Log(object):
    def __init__(self):
        pass

    @staticmethod
    def info(info=''):
        file = FileTools(logFileName)
        file.fileWriteAppend(info)

    @staticmethod
    def deg(debug=''):
        file = FileTools(logFileName)
        file.fileWriteAppend(debug)

    @staticmethod
    def error(error=''):
        file = FileTools(logFileName)
        file.fileWriteAppend(error)

    def info1(self, info=''):
        file = FileTools(logFileName)
        file.fileWriteAppend(info)

    def deg1(self, debug=''):
        file = FileTools(logFileName)
        file.fileWriteAppend(debug)

    def error1(self, error=''):
        file = FileTools(logFileName)
        file.fileWriteAppend(error)
