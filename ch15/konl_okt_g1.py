from konlpy.tag import Okt
from nltk import Text
from konlpy.corpus import kolaw
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

c = kolaw.open('constitution.txt').read()
okt = Okt()
kolaw = Text(okt.nouns(c), name="kolaw")
kolaw.plot(30)
plt.show()