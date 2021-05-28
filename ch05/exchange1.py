def krw_to_usd(won):
    dollars = []
    for i in won:
        dollars.append(i/1000)
    print("미국화폐 :", dollars)
    usd_to_jpy(dollars)

# 달러$ -> 엔화로 바꾸는 함수
def usd_to_jpy(dollars): # 100엔 8$
    yens = []
    for i in dollars:
        yens.append(i * 1000 / 8)
    print("일본 화폐 : ", yens)
amounts = [1000, 2000, 3000, 4000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐 : " + str(amounts))
krw_to_usd(amounts)