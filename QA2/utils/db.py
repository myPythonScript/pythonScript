# *-* coding = utf-8 *-*
"""
连接mysql数据库
"""
# import pymysql
# from dotenv import find_dotenv, load_dotenv
# import os
# load_dotenv(find_dotenv())
# DB_CONF = {
#     "db": os.environ.get("mysql_server"),
#     "host": os.environ.get("mysql_host"),
#     "port": int(os.environ.get("mysql_port")),
#     "user": os.environ.get("mysql_username"),
#     "password": os.environ.get("mysql_passwrod")
# }

# class DB(object):
#     def __init__(self, conf=DB_CONF):
#         self.conn = pymysql.connect(**conf, autocommit=True)
#         self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
#
#     def select_data(self, table_name, column_name, value):
#         self.cur.execute(f'select * from {table_name} where {column_name} = {value}')
#         result = self.cur.fetchall()
#         return result
#
#     def update_data(self, table_name, column_name, new_value, old_value):
#         self.cur.execute(f'update {table_name} set {column_name} = {new_value} where {column_name} = {old_value}')
#
#     # 关闭连接
#     def close(self):
#         self.cur.close()
#         self.conn.close()
#
#
# if __name__ == '__main__':
#     db = DB()
#     res = db.select_data('cardinfo', 'cardNumber', '666888123456')
#     print(res)
#     db.close()

# class DB(object):
#     def find_data(self):
#         self.client = pymongo.MongoClient(
#             "mongodb://192.168.1.89:27017,192.168.1.88:27017,192.168.1.91:27017/")
#         self.db = self.client["qsdb"]
#         self.col = self.db.circle
#         # mongoDB,查找
#         result = self.col.find()
#         return result
#
#
# if __name__ == "__main__":
#     db_mongodb = DB()
#     res = db_mongodb.find_data()
#     print(res)

# 连接mongodb数据库
import pymongo
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())


class DB(object):
    def __init__(self):
        self.client = pymongo.MongoClient(os.environ.get("url"))
        self.db = self.client.qsdb

    def find_data(self, set_name, column_name, column_value):
        col = self.db[set_name]
        rest = col.find({column_name: column_value})
        return rest


if __name__ == "__main__":
    db = DB()
    res = db.find_data("collected", "name", "收藏夹9")
    for i in res:
        print(i["_id"])
    with open("123.txt", "r+", encoding="utf-8") as f:
        data = f.readlines()
        print((data[1].split(":", 1))[1])
