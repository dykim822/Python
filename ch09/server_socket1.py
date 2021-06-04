from socket import *
# 소켓 객체 생성
svrsocket = socket(AF_INET, SOCK_STREAM)    # 소켓 객체 생성
# svrsocket.bind((HOST ip, PORT))    # 소켓을 컴퓨터 포트에 연결
svrsocket.bind(('127.0.0.1', 8000))
svrsocket.listen(1)
conn, addr = svrsocket.accept() # 클라이언트가 연결할 때까지 대기
print(addr)
b = conn.recv(1024) # 클라이언트가 보낸 글 읽기
conn.send("Hello Client".encode())  # 클라이언트에 직렬화해서 보내기
print(b.decode())   # 보낸 메시지를 역직렬화하여 출력하기
conn.close()