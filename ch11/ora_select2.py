import cx_Oracle
con = cx_Oracle.connect("scott/tiger@127.0.0.1:1521/xe")
cur = con.cursor()
cur.execute("select * from emp where empno=7839")
data = cur.fetchall()
for i in data:
    print(i)
cur.close()
con.close()