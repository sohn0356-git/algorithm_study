from itertools import combinations


while True:
    lotto_num = list(map(int, input().split()))

    if lotto_num[0] == 0:
        break

    del lotto_num[0]

    lotto_num = list(combinations(s, 6))
    for i in lotto_num:
        for j in i:
            print(j, end = " ")
        print()
    print()