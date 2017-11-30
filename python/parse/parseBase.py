# -*- coding: UTF-8 -*-
__author__ = 'winter'

class ParseBase(object):
    def __init__(self, content):
        self.content = content
    def setUrl(self, url):
        self.url = url
    # @abs
    def parse(self):
        pass