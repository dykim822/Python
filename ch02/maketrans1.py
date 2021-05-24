instr = 'abcdef'
outstr = '123456'
# instr에 해당 인덱스 문자를 outstr으로 변경할 수 있도록 매핑
trans = ''.maketrans(instr, outstr)
str1 = 'hello world'
# str1문자를 매핑한대로 변경
print(str1.translate(trans))