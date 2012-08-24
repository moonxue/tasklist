#filename:recode.py
#-*- coding:utf8-*-
# a base class to Handler the http Request
# 

import datetime
from pymongo.objectid import ObjectId
import logging
from basemodel import BaseModel


class Recode(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.recode = self.db.recode
      
    def check_user_date(self, _id, user):
        return self.recode.find({"username": user,
                                  "_id": ObjectId(_id)})
        
        
    def update(self, dic, user):
        dic = self.preHandler(dic)
        if dic.get("_id","")=="" :
            #写入新数据
            del dic['_id']
            dic["username"] = user
            dic["date"]=datetime.datetime.utcnow()
            try:
                self.recode.insert(dic)
            except Exception,e:
                logging.error(e)
                return False 
        else:
            #更新已有数据
            #检查要更新的数据和当前登录用户的关系
            if not self.check_user_date(dic['_id'], user):
                logging.error("no relationship between user and the date!")
                return False
            dic['_id'] = ObjectId(str(dic.get("_id","")))
            dic['date'] = datetime.datetime.utcnow()
            try:
                self.recode.save(dic)
            except Exception,e:
                logging.error(e)
                return False
        return True
    
    def finish(self, _id, user):
        if not self.check_user_date(_id, user):
            logging.error("no relationship between user and the date!")
            return False
        try:
            self.recode.update({"_id":ObjectId(str(_id))},{"$set":{"finish":True}})
            return True
        except Exception,e:
            logging.error(e)
            return False
        
    def remove(self,_id, user):
        if not self.check_user_date(_id, user):
            logging.error("no relationship between session['user'] and the date!")
            return False
        try:
            self.recode.remove({"_id":ObjectId(str(_id))})
            return True
        except Exception,e:
            logging.error(e)
            return False
        
    def get(self, user):
        username = user
        #未完成任务
        _list_task = self.recode.find({"finish":{"$nin":[True]}, 'username':username}).sort("date")
        list_task = []
        for item in _list_task:
            if item['tag'] == u"重要":
                item['tag_class'] = "label label-important"
            elif item['tag'] == u"备忘":
                item['tag_class'] = "label label-warning"
            elif item['tag'] == u"普通":
                item['tag_class'] = "label label-info"
            list_task.append(item)
        #已完成任务
        _list_done = self.recode.find({"finish":True,'username':username}).sort("date")
        list_done = []
        for item in _list_done:
            if item['tag'] == u"重要":
                item['tag_class'] = "label label-important"
            elif item['tag'] == u"备忘":
                item['tag_class'] = "label label-warning"
            elif item['tag'] == u"普通":
                item['tag_class'] = "label label-info"
            list_done.append(item)
        return list_task,list_done
        #return  self.recode.find({"status" : None})
        