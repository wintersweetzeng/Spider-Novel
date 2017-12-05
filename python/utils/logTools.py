#-*- conding:UTF-8 -*-
__author__ = 'winter'

from time import ctime

from utils.fileTools import FileTools
from code import systemCode

logFileName = systemCode.baseFolder+u'/'+u'novel.log'
class Log(object):
    def __init__(self):
        pass

    @staticmethod
    def info(info=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Info %s "%(ctime())+info)

    @staticmethod
    def deg(debug=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Debug %s "%(ctime())+debug)

    @staticmethod
    def error(error=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Error %s "%(ctime())+error)

    @staticmethod
    def waring(waring=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Error %s "%(ctime())+waring)

    def info1(self, info=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Info %s "%(ctime())+info)

    def deg1(self, debug=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Debug %s "%(ctime())+debug)

    def error1(self, error=''):
        file = FileTools(logFileName)
        file.fileWriteAppend("Error %s "%(ctime())+error)
