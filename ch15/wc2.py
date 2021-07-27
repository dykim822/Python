from wordcloud import WordCloud
import matplotlib.pyplot as plt
font_path = "c:/Windows/Fonts/malgun.ttf"
text = "사과 수박 수박 수박 수박 수박 대추 대추 복숭아 복숭아 복숭아"
wordcloud = WordCloud(font_path=font_path).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()