sum = 0
# 1부터 101전까지 => 100까지
for i in range(1, 101):
    sum += i
print(f"1부터 {i}까지 합은 {sum}")

# 0부터 4앞까지 => 0~3
for i in range(4):
    print(f"i = {i}", end="")
    for j in range(4):
        print(j, end=" ")
    print()