import socket
# port 번호 확인
print(socket.getservbyname('http', 'tcp'))
print(socket.getservbyname('ftp', 'tcp'))
