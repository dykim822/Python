from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.corpus import kobill
from konlpy.tag import Okt
import nltk
font_path = "c:/Windows/Fonts/malgun.ttf"
# print(kobill.fileids()) # 1809890.txt # 300개
data = kobill.open("1809890.txt").read()
okt = Okt()
nouns = okt.nouns(data)
text = nltk.Text(nouns)
data1 = text.vocab()
data300 = data1.most_common(300)
dic = dict(data300)
wc = WordCloud(width=1000, height=600,background_color='white',
 font_path=font_path)
plt.imshow(wc.generate_from_frequencies(dic))
plt.axis("off")
plt.show()