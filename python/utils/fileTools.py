# -*- coding: UTF-8 -*-
__author__ = 'winter'

import os
class FileTools:
    fileName = "file"
    def __init__(self, fileName):
        self.fileName = fileName
    # @staticmethod
    def readFile(self):
        if not os.path.exists(self.fileName):
            print("Read file %s "%(self.fileName)," file not exist !")
            return ""
        file = open(self.fileName, "rb");
        content =  file.read()
        file.close()
        return  content

    def writeNewFile(self, content):
        file = open(self.fileName, "wb")
        file.write(content)
        file.close()

    def fileWriteAppend(self, content):
        if not os.path.exists(self.fileName):
            file = open(self.fileName, "wb+")
            file.write(content)
            file.write('\r\n')
            file.close()
        else:
            file = open(self.fileName, "ab+")
            file.write(content)
            file.write('\r\n')
            file.close()