import yaml
yaml_str="""
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""
data = yaml.safe_load(yaml_str)
# 이름과 가격 출력하기
for item in data['PriceList']:
    print(item['name'], item['price'])