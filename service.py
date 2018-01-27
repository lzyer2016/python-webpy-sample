#encoding:utf-8

#   业务模块与DB交互

from settings import *

def query_users(userid=''):
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from user"
    if userid != '':
        sql += " where user_id = %s " %(userid)
    cur.execute(sql)
    r = cur.fetchall()
    cur.close()
    conn.close()
    return r