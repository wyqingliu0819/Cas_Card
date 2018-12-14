import pymysql
from conf import config
import logging

def get_con():
    conn = pymysql.connect(host=config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           password=config.db_password,
                           db=config.db_db,
                           charset='utf8')
    return conn

#查询数据库
def db_query(sql):
    logging.info(sql)
    conn = get_con()
    cur = conn.cursor()
    cur.execute(sql)
    r = cur.fetchall()
    cur.close()
    conn.close()
    return r

#修改数据库
def db_change(sql):
    logging.info(sql)
    conn = get_con()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        logging.info(repr(e))
        conn.rollback()       #回滚
    cur.close()
    conn.close()


#查询加油卡是否存在
def check_card(cardNumber):
    r = db_query("select * from cardinfo where cardNumber='%s'" % cardNumber)
    #print(r)
    if r:
        return True
    return False

#删除加油卡
def del_card(cardNumber):
    db_change("delete from cardinfo where cardNumber='%s'" % cardNumber)

#删除绑定的加油卡
#def del_bind_card(cardNumber):
    #db_change("update cardinfo set cardstatus=null, userId=null where cardNumber='%s'" % cardNumber)
#print(check_card("986133222"))
#del_card("9861332")