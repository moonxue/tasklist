#filename:recode.py
#-*- coding:utf8-*-
# a base class to Handler the http Request
# 

import datetime
from pymongo.objectid import ObjectId
import logging
from baseHandler import BaseHandler

class Recode(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.recode = self.db.recode
        
    def update(self, dic):
        dic = self.preHandler(dic)
        if dic.get("_id","")=="" :
            #写入新数据
            del dic['_id']
            dic["date"]=datetime.datetime.utcnow()
            try:
                self.recode.insert(dic)
            except Exception,e:
                logging.error(e)
                return False 
        else:
            #更新已有数据
            dic['_id'] = ObjectId(str(dic.get("_id","")))
            dic['date'] = datetime.datetime.utcnow()
            try:
                self.recode.save(dic)
            except Exception,e:
                logging.error(e)
                return False
        return True
    
    def finish(self,_id):
        try:
            self.recode.update({"_id":ObjectId(str(_id))},{"$set":{"finish":True}})
            return True
        except Exception,e:
            logging.error(e)
            return False
        
    def remove(self,_id):
        try:
            self.recode.remove({"_id":ObjectId(str(_id))})
            return True
        except Exception,e:
            logging.error(e)
            return False
        
    def get(self):
        #未完成任务
        _list_task = self.recode.find({"finish":{"$nin":[True]}}).sort("date")
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
        _list_done = self.recode.find({"finish":True}).sort("date")
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
        