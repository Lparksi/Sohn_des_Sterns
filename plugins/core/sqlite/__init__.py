import os
import sqlite3


def __config_statistics():
    c = Sohn_des_Sterns.cursor()
    c.execute('insert into statistics (item, value) values ("existing_users",0)')
    c.execute('insert into statistics (item, value) values ("registered_user",0)')
    c.execute('insert into statistics (item, value) values ("delete_users",0)')
    c.execute('insert into statistics (item, value) values ("total_money",0)')
    Sohn_des_Sterns.commit()


# 创建 db 文件夹
if not os.path.isdir('db'):
    os.mkdir('db')

Sohn_des_Sterns = sqlite3.connect('db/Sohn_des_Sterns.db')

tables = Sohn_des_Sterns.cursor().execute("select * from sqlite_master").fetchall()

# 获取已存在表列表
table_list = []
for table in tables:
    table_list.append(table[2])

if 'statistics' not in table_list:
    with open('plugins/core/sqlite/sql/statistics.sql', 'r') as f:
        Sohn_des_Sterns.cursor().execute(f.read())
    __config_statistics()

if 'user' not in table_list:
    with open('plugins/core/sqlite/sql/user.sql', 'r') as f:
        Sohn_des_Sterns.cursor().execute(f.read())

__all__ = ['Sohn_des_Sterns']
