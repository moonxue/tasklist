#filename:user.py
#-*- coding:utf8-*-

import datetime
import logging as log
from hashlib import md5
from pymongo.objectid import ObjectId 
from basemodel import BaseModel


class User(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.user = self.db.user
        
    def update(self, dic):
        dic = self.preHandler(dic)
        if dic.get("user","")=="" :
            #写入新数据
            dic["date"]=datetime.datetime.utcnow()
            dic['pw'] = md5(dic['pw']+self.salt).hexdegiest()
            try:
                self.user.insert(dic)
            except Exception,e:
                log.error(e)
                return False 
        else:
            #更新已有数据
            try:
                dic['pw'] = md5(dic['pw']+self.salt).hexdegiest()
                self.user.save(dic)
            except Exception,e:
                log.error(e)
                return False
        return True 
    
    def hasUser(self, user):
        result = self.user.find_one({'username':user})
        if result:
            return True
        else:
            return False
        
    def checkUser(self,user,pw):
        result = self.user.find_one({'username':user, 'pw': md5(pw+self.salt).hexdigest()})
        log.warn(result)
        if result:
            return True
        else:
            return False
        