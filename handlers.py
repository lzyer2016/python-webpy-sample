#encoding:utf-8

#   处理模块
import web
import json
from service import *

#定义全局渲染
render = web.template.render('templates') 

class api:
    def GET(self):
        param = web.input()
        if param.has_key('id'):
            r = query_users(param.id)
        else:
            r = query_users()
        web.header('content-type','text/json')
        return json.dumps(r)
class users:
    def GET(self,name="users"):
        try:
            if name != "users":
                if name.startswith('/'):
                    userid = name[1:]
            r = query_users(userid)
            return render.users(r)#users.html
        except Exception, e:
            print e.message
class redirect:
    def GET(self):
        query = web.input()
        #页面跳转
        return web.seeother('https://www.baidu.com')
class blog:
    def GET(self):
        #获取请求头
        return web.ctx.env
    def POST(self):
        #获取参数
        data = web.input()
        return "login success username=" +str(data.username)+"& password="+str(data.password)      
class index:        
    def GET(self, name):
        r = query_users()
        return render.index(name)#demo.html