import pandas as pd
import pymysql, sys
con = pymysql.connect(host='127.0.0.1', port=3306, user='root',
passwd='mysql', db='test', charset ='utf8')
list = []
try:
    cursor = con.cursor()
    cursor.execute("select * from dept order by deptno")
    data = cursor.fetchall()
    for i in data:
        list.append(i)
except :
    print('에러 : ',sys.exc_info())
finally:
    con.close()
df = pd.DataFrame(list)
print(df)