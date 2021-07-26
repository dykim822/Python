import pandas as pd
import pymysql, sys
con = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                      passwd='mysql', db='test', charset='utf8') # utf-8이 아님
list = []
try:
    cursor = con.cursor()
    cursor.execute("select date, name,price, count from stock")
    data = cursor.fetchall()
    for i in data:
        list.append(i)
except:
    print('에러 :',sys.exc_info())
finally:
    con.close()
df = pd.DataFrame(list, columns=['date', 'name', 'price', 'count'])
print(df)
print(df.pivot('date','name'))