#       01234
str1 = "Korea"
#    -5-4-3-2-1
print(str1[0])          # 인덱스 0
print(str1[-2])         # 인덱스 -2
print(str1[1:3])        # 인덱스 1부터 3앞까지 => 인덱스 1, 2
print(str1[0:5:2])      # 인덱스 0부터 5앞까지 2칸씩 띄어서 출력=> 인덱스 0, 2, 4
print(str1[:-1])        # 인덱스 처음부터 마지막 글자를 제외하고 전부 출력
print(str1[::-1])       # 처음부터 끝까지 거꾸로 출력

str2 = "Hello" + "World"
print(str2)     # 두 문자열을 합친다
print(str2 * 3)