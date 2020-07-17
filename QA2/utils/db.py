""""""
# *-* coding = utf-8 *-*
import pymysql
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
DB_CONF = {
    "db": os.environ.get("mysql_server"),
    "host": os.environ.get("mysql_host"),
    "port": int(os.environ.get("mysql_port")),
    "user": os.environ.get("mysql_username"),
    "password": os.environ.get("mysql_passwrod")
}


class DB(object):
    def __init__(self, conf=DB_CONF):
        self.conn = pymysql.connect(**conf, autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def select_data(self, table_name, column_name, value):
        self.cur.execute(f'select * from {table_name} where {column_name} = {value}')
        result = self.cur.fetchall()
        return result

    def update_data(self, table_name, column_name, new_value, old_value):
        self.cur.execute(f'update {table_name} set {column_name} = {new_value} where {column_name} = {old_value}')

    # 关闭连接
    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    res = db.select_data('cardinfo', 'cardNumber', '666888123456')
    print(res)
    db.close()