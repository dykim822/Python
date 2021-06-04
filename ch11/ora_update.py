import cx_Oracle, sys
try:
    con = cx_Oracle.connect("scott/tiger@127.0.0.1:1521/xe")
    cur = con.cursor()
    cur.execute("update dept set dname='광고' where deptno=17")
    con.commit();
    print("수정 성공")
except:
    print("에러 : ", sys.exc_info())
finally:
    cur.close()
    con.close()