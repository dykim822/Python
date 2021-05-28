def print_square(x):
    print(x * x)
def get_square(x):
    return x * x
print_square(7) # 49
print("--")     # --
get_square(5)   # print는 안함
print("--")     # --
print(get_square(5))    # 25
print("--")             # --
print(print_square(7))  # 49