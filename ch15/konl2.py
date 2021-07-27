from konlpy.tag import Hannanum, Kkma, Komoran,Okt
from konlpy.corpus import kolaw
c = kolaw.open('constitution.txt').read()
hannanum = Hannanum()
kkma = Kkma()
kormoran = Komoran()
okt = Okt()
print('한나눔',hannanum.nouns(c[:40]))
print('kkma',kkma.nouns(c[:40]))
# komorna은 빈줄이 에러가 발생
print('komoran', kormoran.nouns("\n".join([s for s in c[:40].split("\n") if s])))
print("Okt", okt.nouns(c[:40]))