import pymysql, sys

import pymysql
try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',
                          db='test', charset='utf8')
    cursor = con.cursor()   # sql을 사용하기 위한 객체
    cursor.execute("update dept set dname='관리' where deptno=13")
    con.commit()
    print("수정 성공")
except:
    print("에러 :", sys.exc_info())
finally:
    cursor.close()
    con.close()