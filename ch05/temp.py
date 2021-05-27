# 섭씨온도 - 화씨온도 변환
def fahrenheit_to_celsius(fahrenheit):
    print("화씨 온도 리스트 : ", fahrenheit)
    c = []
    for i in fahrenheit:
        k = (i - 32) * 5 / 9
        c.append(k)
    print("섭씨 온도 리스트 : ", c)
# test용 화씨 온도 리스트
sample_temperature_list = [40, 14, 32, 64, -4, 11]
# 섭씨온도 출력
fahrenheit_to_celsius(sample_temperature_list)