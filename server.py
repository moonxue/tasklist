#!/usr/bin/env python
#filename:server.py
#-*- coding:utf8-*-
# a test script for bottle framework
# 
import sys
import os
from bottle import run, template,route, static_file, TornadoServer, request, redirect
from recode import Recode

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

@route('/css/<filename:path>')
def cssHandler(filename):
    return static_file(filename, root="css")

@route('/js/<filename:path>')
def jsHandler(filename):
    return static_file(filename, root="js")
                
@route('/img/:<filename:path>')
def imgHandler(filename):
    return static_file(filename, root="img")

@route('/update_recode', method="POST")
def recode_UpdateHandler():
    dic = dict(request.forms)
    result = recode.update(dic)
    if not result :
        return "faild"
    redirect('/')
    return

@route('/finish/:_id')
def recode_FinishHandler(_id):
    result = recode.finish(_id)
    if not result :
        return "faild"
    redirect('/')
    return

@route('/remove/:_id')
def recode_RemoveHandler(_id):
    result = recode.remove(_id)
    if not result :
        return "faild"
    redirect('/')
    return

@route('/')
def homeHandler():
    list_task,list_done = recode.get()
    return template("tasklist.tpl",list_task=list_task,list_done=list_done)

recode=Recode()
run(host = "localhost",port=8080,server=TornadoServer)


