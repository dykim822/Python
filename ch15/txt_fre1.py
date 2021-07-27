from nltk import Text
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt") # 문서가져오기
retokenize = RegexpTokenizer("[\w]+") # 문자 숫자만 추출
text = Text(retokenize.tokenize(emma_raw), name="Emma")
text.plot(20) # 상우; 20개
plt.show()