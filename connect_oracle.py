#coding=utf-8
import os
import cx_Oracle
import sys
import importlib
importlib.reload(sys)

os.environ['NLS_LANG'] = 'TRADITIONAL CHINESE_TAIWAN.AL32UTF8'

TNAME = "'GG'"
VALUES = "'GG'"
conn = cx_Oracle.connect("apuser", "apuser", "192.168.255.105:1521/orcl")
cur = conn.cursor()
sql = '' # oracle sql語句
print(sql)
cur = conn.cursor()
cur.execute(sql)
conn.commit()
'''rows = cur.fetchall()
for row in rows:
  print(row)'''
