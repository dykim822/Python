data = """
park 800905-1049118
kim 700905-1059119
"""
result = []
for line in data.split("\n"):   # __, park 800905-1049118, kim 700905-1059119, __
    word_result = []
    for word in line.split(" "):    # [[park, 800905-1049118], [kim 700905-1059119]]
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)    #[""], [park, 800905-*******], [kim, 700905-*******], [""]
    result.append(" ".join(word_result))
print("\n".join(result))
