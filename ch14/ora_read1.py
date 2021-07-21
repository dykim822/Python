import cx_Oracle, sys
import pandas as pd
con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
list = []
try:
    cursor = con.cursor()
    cursor.execute("select * from dept order by deptno")
    data = cursor.fetchall()
    for i in data:
        list.append(i)
except:
    print('예외 :',sys.exc_info())
finally:
    con.close()
df = pd.DataFrame(list, columns=['부서코드','부서명','근무지'])
print(df)