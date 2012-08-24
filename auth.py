#!/usr/bin/env python
#filename:auth.py
#-*- coding:utf8-*-
from bottle import run, template,route, static_file, \
TornadoServer, request, redirect, default_app

def checkauth(func):
    def wrapper():
        s = request.environ.get('beaker.session')
        user = s.get("user","")
        pw = s.get("pw","")
        if
        
def login(user,pw):
    

