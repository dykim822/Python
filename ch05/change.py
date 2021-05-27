def calculat_change(payment, cost):
    val = payment - cost    # val: 거스름돈
    unit = [50000, 10000, 5000, 1000]
    for i in unit:
        print(f"{i}원 : {val // i}장")
        val = val % i
# Test
calculat_change(100000, 33000)
print()
calculat_change(500000, 378000)