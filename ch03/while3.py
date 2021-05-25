i = 1
j = 2
while i < 10:
    while j < 10:
        print(f"{j} * {i} = {i * j}", end="\t")
        j += 1
    print()
    i += 1
    j = 2