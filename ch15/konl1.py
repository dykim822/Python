from konlpy.corpus import kolaw
print(kolaw.fileids())
c = kolaw.open('constitution.txt').read()
print(c[:40])