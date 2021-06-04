from socket import *
svrsocket = socket(AF_INET, SOCK_STREAM)    # ipv4, tcp/ip 방식
print("서버 가동중 ...")
svrsocket.bind(('172.30.1.44', 7001))   # 소켓과 서버와 연결
while True:
    svrsocket.listen(20)    # 20명까지 연결 가능
    conn, addr = svrsocket.accept() # 클라이언트 연결할 때까지 대기
    print(addr) # 지금 연결된 고객 ip출력
    b = conn.recv(1024) # 고객이 보낸 데이터 받기
    conn.send(b)
    print(b.decode())   # 받은 데이터 출력
conn.close()