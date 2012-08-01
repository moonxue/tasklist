#filename:baseHandler.py
#-*- coding:utf8-*-
# a base class to Handler the http Request
# 

import pymongo

class BaseHandler:
    def __init__(self):
        connection=pymongo.Connection('localhost',27017)
        self.db=connection.pynote
        
    def preHandler(self,dic):
        #去掉转义字符
        _dic={}
        for k,v in dic.items():
            v=v.replace('&lt;','<')
            v=v.replace('&gt;','>')
            v=v.replace('&amp;','&')
            v=v.replace('&quot;','"')
            _dic[k]=v
        return _dic 