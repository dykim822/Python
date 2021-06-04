import pymysql, sys
try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',
                          db='test', charset='utf8')
    cursor = con.cursor()   # sql을 사용하기 위한 객체
    cursor.execute("select * from dept order by deptno")
    data = cursor.fetchall()
    # print(data)
    for i in data:
        print(i)
except:
    print("에러 :", sys.exc_info())
finally:
    cursor.close()
    con.close()