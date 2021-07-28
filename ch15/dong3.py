import pytagcloud
# with와 같이 사용하면 close를 안해도 된다
with open('count.txt', 'r', encoding='utf-8') as f:
    input_data = f.readlines()
    data = []
    for d in input_data:
        d0, d1 = d.split() # do: 단어 d1:갯수
        if len(d0) > 1: # 2글자 이상
            data.append((d0, int(d1)))
    print(data)
    tag_list = pytagcloud.make_tags(data, maxsize=100)
    pytagcloud.create_tag_image(tag_list,"dong1.png",
            size=(900, 600), fontname="Korean", rectangular=False)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("dong1.png")
imgplot = plt.imshow(img)
plt.axis("off")
plt.show()