#!/usr/bin/env python
#filename:server.py
#-*- coding:utf8-*-
# a test script for bottle framework
# 
import sys
import os
import logging as log
from flask import Flask, url_for, make_response, redirect, request
from bottle import template
from recode import Recode
from beaker.middleware import SessionMiddleware
from forms.user_login import User_login
from user import User

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
session_opts = {
                'session.type':'file',
                'session.cookei_expires':300,
                'session.data_dir':'./sessions',
                'sessioni.auto':True
                }
recode = Recode()
app = Flask(__name__)
app.secret_key="MoonXue"
route = app.route
app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
user = User()


def static_file(filename,root): 
    url = os.path.abspath('.')+"/static/"+root+'/'+filename
    content = open(url).read()
    if root == "css" :
        type = "text/css"
    elif root == "image":
        type = "image/"+filename.splite('.')[-1]
    elif root == "js":
        type = "txt/javascript"
    response = make_response(content)
    response.mimetype=type
    return response

    
@route('/css/<path:filename>')
def cssHandler(filename):
    return static_file(filename, root="css")


@route('/js/<path:filename>')
def jsHandler(filename):
    return static_file(filename, root="js")

                
@route('/img/<path:filename>')
def imgHandler(filename):
    return static_file(filename, root="img")


@route('/update_recode', methods=["POST"])
def recode_UpdateHandler():
    session = request.environ['beaker.session']
    dic = dict(request.form)
    _dic = {}
    for k,v in dic.items():
        _dic[k]=v[0]
    dic = _dic
    result = recode.update(dic, session['user'])
    if not result :
        return "faild"
    return redirect('/')


@route('/finish/<_id>')
def recode_FinishHandler(_id):
    session = request.environ['beaker.session']
    result = recode.finish(_id, session['user'])
    if not result :
        return "faild"
    return redirect('/')


@route('/remove/<_id>')
def recode_RemoveHandler(_id):
    session = request.environ['beaker.session']
    result = recode.remove(_id, session['user'])
    if not result :
        return "faild"
    return  redirect('/')


@route('/', methods=['POST','GET'])
def homeHandler():
    session = request.environ['beaker.session']
    form =User_login(secret_key="MoonXue")
    if session.has_key('user'):
        list_task,list_done = recode.get(session['user'])
        return template("tasklist.tpl",list_task=list_task,list_done=list_done)
    else:
        return redirect("/login")
    
    
@route('/login',methods=['POST','GET'])
def loginHandler():
    session = request.environ['beaker.session']
    form =User_login(secret_key="MoonXue")
    if not session.has_key('user'):
        if request.method == "GET":
            log.warn('get')
            return template("login.tpl",form=form)
        else:
            log.warn('post')
            username = request.form['username']
            pw = request.form['pw']
            log.warn(username)
            log.warn(pw)
            if user.checkUser(username, pw):
                session['user'] = username
                log.warn('ok')
                session.save()
                return redirect('/')
            else:
                return template("login.tpl",form=form)
    else:
        return redirect("/")    
    
    
if __name__ == "__main__":
    app.run(host='222.20.79.207', port=8080)


