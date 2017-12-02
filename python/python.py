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

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template(systemCode.baseFolder+u'/index.html',title = 'Home')
    # return systemCode.baseFolder+u'/index.html'  http://www.jb51.net/article/64452.htm

@app.route('/LoveNovel/updateNovel', methods=['POST', 'GET'])
def updateNovel():
    spider = SpiderMannager()
    spider.updateNovel()
    return jsonify(systemCode.responseSucc)


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

# spider = SpiderMannager()
# updateNovelThreads = []
# updateThread = threading.Thread(target=spider.manager(),args=())
# updateNovelThreads.append(updateThread)


if __name__ == '__main__':
    app.run(host=systemCode.host, port='5000', debug=False)
    # for thread in updateNovelThreads:
    #     thread.setDaemon(False)
    #     thread.start()



