import pymysql
# DB 연결
con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql',
                      db='test', charset='uft8')
print(con)
con.close()