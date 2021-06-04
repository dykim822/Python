from socket import *
sock = socket(AF_INET, SOCK_DGRAM)
print('메세지를 입력하세요')
msg = input()
sock.sendto(msg.encode(), ('172.30.1.44', 7003))
s, addr = sock.recvfrom(1024)
print(s.decode())
print(addr)
sock.close()