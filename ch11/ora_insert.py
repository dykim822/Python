import cx_Oracle, sys
try:
    con = cx_Oracle.connect("scott/tiger@127.0.0.1:1521/xe")
    cur = con.cursor()
    cur.execute("insert into dept values(17, '홍보', '마포')")
    con.commit();
    print("입력 성공")
except:
    print("에러 : ", sys.exc_info())
finally:
    cur.close()
    con.close()