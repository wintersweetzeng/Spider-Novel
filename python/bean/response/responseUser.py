#-*- conding:UTF-8 -*-
__author__ = 'winter'

class ResponseUser(object):
    id = ''
    name = ''
    pwd = ''
    org = ''
    def __init__(self, id, name, pwd, org):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.org = org

