from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('172.30.1.44', 7002)) # 서버와 연결
print('전달할 메세지를 입력하세요')
msg = input()
sock.send(msg.encode())
b = sock.recv(1024)
print(b.decode())
sock.close()