file = open('bin.txt', 'wb')
file.write('안녕하세요'.encode())
file.close()
file = open('bin.txt', 'rb')
txt = file.read()
# print(txt)    바이너리 코드로 출력된다
print(txt.decode()) # encode해줬으므로 읽을 때 decode해줘야 한다
file.close()