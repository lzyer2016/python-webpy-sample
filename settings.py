#encoding:utf-8

#   setting模块

import MySQLdb
import MySQLdb.cursors

host='localhost'
user='root'
passwd='123456'
db='auth'
port=3306
charset='utf8'
cursorclass=MySQLdb.cursors.DictCursor

def getconn():
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd,db=db, 
        port=port,charset=charset,cursorclass=cursorclass)
    return conn