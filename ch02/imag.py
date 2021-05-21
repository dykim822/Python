c = 3 + 4j
print(c)
a = 3
b = 4
# complex(실수부, 허서부) -> a+bi 꼴
print(complex(a, b))
# conjugate 켤레복소수 -> a-bi
d = c.conjugate()
print(d)
e = d * c
print(e)