from nltk import Text
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer
emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt") # 문서가져오기
retokenize = RegexpTokenizer("[\w]+") # 문자 숫자만 추출
text = Text(retokenize.tokenize(emma_raw), name="Emma")
# dispersion_plot 메서드 안에 있는 단어가 사용된 위치를 시갓화
text.dispersion_plot(["Emma","Knightley","Frank","Jane","Harriet","Robert"])
# 해당 단어가 사용된 문맥 5개
text.concordance("Emma", lines=5)
# 해당 단어와 미슷한 문백에서 사용된 단어
text.similar("Emma", 10)
plt.show()