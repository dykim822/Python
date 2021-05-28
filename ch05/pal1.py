def is_palindrome(word):
    # reword = word[::-1]   (1) 가장 쉬운 방법
    reword = ""
    # for i in range(1, len(word) + 1): (2) 두번째 방법
    #     reword += word[-i]

    # 마지막 인덱스부터 인덱스 0까지 1씩 감소하며 반복
    for i in range(len(word) - 1, -1, -1):
        reword += word[i]
    return reword == word
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
#                    0123
print(is_palindrome("토마토"))
#                   -3-2-1
print(is_palindrome("kayak"))
print(is_palindrome("hello"))