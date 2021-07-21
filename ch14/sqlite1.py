import sqlite3
import pandas as pd
dbpath = 'test.sqlite'
conn = sqlite3.connect(dbpath)
cur = conn.cursor()
cur.executescript("""
    drop table if exists items;
    create table items (item_id integer primary key,name text, price integer);
    insert into items(name, price) values('apple', 800);
    insert into items(name, price) values('orange', 780);
    insert into items(name, price) values('banana', 430);    
""")
conn.commit()
list =[]
cur = conn.cursor()
cur.execute("select * from items")
data = cur.fetchall()
for i in data:
    list.append(i)
df = pd.DataFrame(list, columns=['item_id','name','price'])
print(df)
cur.close()
conn.close()