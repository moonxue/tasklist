from flask.ext.wtf import Form, TextAreaField, SubmitField, TextField, \
        ValidationError, required, email, url, optional
        
class User_register(Form):
    user = TextField(u"用户名:", validator=[required(message="u用户名，这个必须有")])
    pw =  PassWordField(u"密码:", validator=[required(message=u"密码，这个也是必须有")])
    email = flask.ext.wtf.html5.EmailInput(u'email:')
    submit = SubmitField(_("注册"))
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None
        
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        ok = checkuser(user=self.user.data)
        if not ok:
            self.user.errors.append(u"未知用户名")
            return False
        ok = checklgoin(user=self.user.data, pw=self.pw.data)
        if not ok:
            self.pw.errors.append(u"用户名和密码不相符")
            return False
        self.user = {"user": self.user.data, "pw": self.pw.data}
        return True