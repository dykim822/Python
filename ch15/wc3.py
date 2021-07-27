from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
font_path = "c:/Windows/Fonts/malgun.ttf"
text = """
 사과 수박 수박 수박 수박 수박 대추 대추 복숭아 복숭아 복숭아
 키위 바나나 바나나 바나나 바나나 곶감 곶감 곶감
 """
stop = set(STOPWORDS)
stop.add("사과")
stop.add("곶감")
wordcloud = WordCloud(font_path=font_path, stopwords=stop).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()