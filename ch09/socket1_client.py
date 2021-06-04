from socket import *
#               ipv4       tcp/ip
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 8000))   # 서버와 연결
sock.send("Hello Server".encode())  # 서버에 보내기
b = sock.recv(1024) # 서버에서 보낸 데이터 1024byte 읽기
print(b.decode())
sock.close()