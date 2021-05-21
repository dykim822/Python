# 작은 따옴표를 출력하기 위해서는 큰 따옴표로 묶어야한다
str1 = "Python's favorite food is perl"
print('str1 = ', str1)
# 작은 따옴표를 출력하려면 \'으로 출력!
str2 = 'Python\'s favorite food is perl'
print('str2 = ', str2)
# 문장 속에 큰 따옴표가 있을 경우에는 밖을 작은 따옴표로 한다
str3 = '"Python is very easy." he says.'
print('str3 = ', str3)
# 밖을 큰 따옴표로 했을 경우에는 \를 추가한다
str4 = "\"Python is very easy.\" he says."
print('str4 = ', str4)