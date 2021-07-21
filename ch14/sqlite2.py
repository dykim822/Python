import sqlite3
import pandas as pd
dbpath = 'test.sqlite'
conn = sqlite3.connect(dbpath)
while True:
    print('과일명 ?')
    fruit = input()
    if fruit=='x':
        break
    print('가격은 ?')
    price = int(input())
    sql = "insert into items(name, price) values(?,?)"
    cur = conn.cursor()
    cur.execute(sql,(fruit, price))
    conn.commit()
sql2 = "select * from items"
cur.execute(sql2)
list = []
items = cur.fetchall()
for i in items:
    list.append(i)
df = pd.DataFrame(list, columns=['아이디','과일명','가격'])