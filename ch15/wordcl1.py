from wordcloud import WordCloud
import nltk
from konlpy.tag import Okt
from nltk import Text
from konlpy.corpus import kolaw
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
plt.rcParams['axes.unicode_minus'] = False
data = kolaw.open('constitution.txt').read()
okt = Okt()
nouns = okt.nouns(data)
text = nltk.Text(nouns)
data1 = text.vocab()
# 단어의 빈도 순서로 상위 500
data500 = data1.most_common(100)
# 데이터를 dictionary형태로 변경
dic = dict(data500)

wc = WordCloud(width=1000, height=600, background_color='white', font_path=font_path)
plt.imshow(wc.generate_from_frequencies(dic))
plt.axis("off") # x/y축 표시하지 마라
plt.show()