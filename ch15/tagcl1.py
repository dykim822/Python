import pytagcloud
from collections import Counter
nouns = list()
# 불고기 8회
nouns.extend(['불고기' for t in range(8)])
nouns.extend(['비빔밥' for t in range(2)])
nouns.extend(['김치찌게' for t in range(20)])
nouns.extend(['돈까스' for t in range(3)])
nouns.extend(['순두부' for t in range(30)])
nouns.extend(['짬뽕' for t in range(2)])
nouns.extend(['짜장' for t in range(28)])
nouns.extend(['삼겹살' for t in range(8)])
nouns.extend(['초밥' for t in range(12)])
nouns.extend(['우동' for t in range(8)])
count = Counter(nouns) # 단어별 횟스 집계
tag2 = count.most_common(10) # 갯수 순위로 상위 19건 추출
# 갯수에 따른 글자 크기 정해 준다
taglist = pytagcloud.make_tags(tag2, maxsize=50) # 글자 최대크기 50px
print(taglist)
pytagcloud.create_tag_image(taglist,'wordclod.jpg', size=(900, 600),
                            fontname='Korean', rectangular=False)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('wordclod.jpg')
imgplot = plt.imshow(img)
plt.show()