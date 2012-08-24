#!/usr/bin/env python
#coding=utf-8
#filename:suser_login.py
# a test script for bottle framework
# 
from flask.ext.wtf import Form, TextAreaField, SubmitField,\
 TextField,ValidationError, required, email, url, optional, PasswordField, validators
from user import User

user = User()
hasUser = user.hasUser
checkUser = user.checkUser

class User_login(Form):
    username = TextField(u"用户名:",[validators.required(message=u"用户名，这个必须有")])
    pw =  PasswordField(u"密码:", [validators.required(message=u"密码，这个也是必须有")])
    submit = SubmitField(u"登录")
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        ok = hasUser(user=self.user.data)
        if not ok:
            self.user.errors.append(u"未知用户名")
            return False
        ok = checkUser(user=self.user.data, pw=self.pw.data)
        if not ok:
            self.pw.errors.append(u"用户名和密码不相符")
            return False
        self.user = {"user": self.user.data, "pw": self.pw.data}
        return True