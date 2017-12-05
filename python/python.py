# -*- coding: UTF-8 -*-

import sys, json, os, threading
from flask import Flask, request,render_template,jsonify

from utils.fileTools import FileTools
from utils.logTools import Log
from code import systemCode
from spiderMannager import SpiderMannager
from requestMannager.requestsMannager import RequestMannager


app = Flask(__name__)

reload(sys)
sys.setdefaultencoding( "utf-8" )

requestMannager = RequestMannager()

##  /LoveNovel/getNovels
## request
# header:content-type json
# body:{"count":10}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
# [
#     {
#         "author": "辰东",
#         "imageurl": "http://www.bixia.org/BookFiles/BookImages/shengxu.jpg",
#         "lashUpdateTime": "2017/12/2 2:35:07",
#         "lastUpdateChapter": "第七百八十九章 神兽血浇灌",
#         "name": "圣墟",
#         "no": "27_27047",
#         "url": "http://www.bixia.org/27_27047/"
#     }
# ]
@app.route('/LoveNovel/getNovels', methods=['POST', 'GET'])
def getNovels():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        count = dict["count"]
        result1 = requestMannager.getNovels()
        return jsonify(result1)
    else:
        return systemCode.responseMethodError

##  /LoveNovel/getChapterList
## request
# header:content-type json
# body:{"novelNo":"27_27047"}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
#[
# {
#     "chapterNo": "第一章",
#     "chapterSourceUrl": "",
#     "chapterTitle": "沙漠中的彼岸花"
# },
# {
#     "chapterNo": "第二章",
#     "chapterSourceUrl": "",
#     "chapterTitle": "后文明时代"
# },
# ]
@app.route('/LoveNovel/getChapterList', methods=['POST', 'GET'])
def getChapterList():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        novelNo = dict["novelNo"]
        result = requestMannager.getChapterList(novelNo)
        return jsonify(result)
    else:
        return systemCode.responseMethodError

##  /LoveNovel/addOneNovel
## request
# header:content-type json
# body:{"novelNo":"27_27047"}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
#"{\"code\":0, \"msg\":success\"}"
#"{\"code\":1, \"msg\":operate is failed\"}"
@app.route('/LoveNovel/addOneNovel', methods=['POST', 'GET'])
def addOneNovel():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        novelNo = dict["novelNo"]
        ok = requestMannager.addOneNovel(novelNo)
        if ok :
            return jsonify(systemCode.responseSucc)
        else:
            return jsonify(systemCode.responseError)
    else:
        return systemCode.responseMethodError


##  /LoveNovel/getChapter
## request
# header:content-type json
# body:{"novelNo":"27_27047","chapterNo":"第一章", "chapterTitle":"沙漠中的彼岸花"}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
# {
#     "content": "\t\t\t\t大漠孤烟直，长河落日圆。<br/>　　<br/>　　&nbsp;&nbsp;&nbsp;&nbs"
# }
@app.route('/LoveNovel/getChapter', methods=['POST', 'GET'])
def getChapter():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        novelNo = dict["novelNo"]
        chapterNo = dict["chapterNo"]
        chapterTile = dict["chapterTitle"]
        result = requestMannager.getChapter(novelNo, chapterNo, chapterTile)
        return jsonify(result)
    else:
        return systemCode.responseError


@app.route('/LoveNovel/updateNovel', methods=['POST', 'GET'])
def updateNovel():
    spider = SpiderMannager()
    spider.updateNovel()
    return jsonify(systemCode.responseSucc)


##  /LoveNovel/getChapterSourceList
## request
# header:content-type json
# body:{"novelNo":"167_167729"}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
#[
# {
#     "chapterSourceUrl": "http://www.bixia.org/167_167729/167_167729/8536700.html",
#     "titleName": "110快来这有作者偷懒了!"
# },
# {
#     "chapterSourceUrl": "http://www.bixia.org/167_167729/167_167729/8536701.html",
#     "titleName": "1 入职"
# }
# ]
@app.route('/LoveNovel/getChapterSourceList', methods=['POST', 'GET'])
def getChapterSourceList():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        novelNo = dict["novelNo"]
        result = requestMannager.getChapterSourceList(novelNo)
        return jsonify(result)
    else:
        return systemCode.responseMethodError


##  /LoveNovel/registry
## request
# header:content-type json
# body:{"name":"zeng","pwd":"123456","org":"Super" }
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#    "{\"code\":11, \"msg\":"already registry error\"}"
#    "{\"code\":10, \"msg\":"org error\"}"
#    "{\"code\":12, \"msg\":"name or password is null\"}"
#succ
#{
#    "id": 151248645273533,
#    "name": "zeng",
#    "org": "Super",
#    "pwd": "zeng"
#}
@app.route('/LoveNovel/registry', methods=['POST', 'GET'])
def registry():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        username = dict["name"]
        password = dict["pwd"]
        org = dict["org"]
        result = requestMannager.registry(username, password, org)
        return jsonify(result)
    else:
        return systemCode.responseMethodError


##  /LoveNovel/login
## request
# header:content-type json
# body:{"name":"liu","pwd":"123456" }
## response
#error "{\"code\":22, \"msg\":"this name not registry\"}"
#    "{\"code\":20, \"msg\":"name or password is null\"}"
#    "{\"code\":21, \"msg\":"name or password is error\"}"
#succ
#"{\"code\":0, \"msg\":\"success\", \"id\":\"151248720783409\"}"
@app.route('/LoveNovel/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        username = dict["name"]
        password = dict["pwd"]
        result = requestMannager.login(username, password)
        return jsonify(result)
    else:
        return systemCode.responseMethodError


##  /LoveNovel/userGetChapter
## request
# header:content-type json
# body:{"novelNo":"27_27047","chapterNo":"第一章", "chapterTitle":"沙漠中的彼岸花","id":"151248685702069"}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
# {
#     "content": "\t\t\t\t大漠孤烟直，长河落日圆。<br/>　　<br/>　　&nbsp;&nbsp;&nbsp;&nbs"
# }
@app.route('/LoveNovel/userGetChapter', methods=['POST', 'GET'])
def userGetChapter():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        novelNo = dict["novelNo"]
        chapterNo = dict["chapterNo"]
        chapterTile = dict["chapterTitle"]
        id = dict["id"]
        result = requestMannager.userGetChapter(novelNo, chapterNo, chapterTile, id)
        return jsonify(result)
    else:
        return systemCode.responseError

##  /LoveNovel/queryUserReadChapter
## request
# header:content-type json
# body:{"novelNo":"27_27047","id":"151248685702069"}
## response
#error {"code":1000, "msg":"unsupport GET method, please use POST"}
#succ
#[
#    {
#        "chapterNo": "第一章",
#        "chapterTitle": "沙漠中的彼岸花",
#        "id": "151248685702069",
#        "novelNo": "27_27047"
#    }
#]
@app.route('/LoveNovel/queryUserReadChapter', methods=['POST', 'GET'])
def queryUserReadChapter():
    if request.method == 'POST':
        data = request.get_data()
        dict = json.loads(data)
        novelNo = dict["novelNo"]
        id = dict["id"]
        result = requestMannager.queryUserReadChapter(novelNo, id)
        return jsonify(result)
    else:
        return systemCode.responseError

# spider = SpiderMannager()
# updateNovelThreads = []
# updateThread = threading.Thread(target=spider.manager(),args=())
# updateNovelThreads.append(updateThread)



if __name__ == '__main__':
    app.run(host=systemCode.host, port='5000', debug=False)
    # for thread in updateNovelThreads:
    #     thread.setDaemon(False)
    #     thread.start()



