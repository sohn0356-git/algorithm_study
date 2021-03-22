# import sys
#
# while True:
#     # 소문자 대문자 숫자 공백
#     up = 0
#     low = 0
#     num = 0
#     spa = 0
#
#     st = sys.stdin.readline().rstrip('\n')
#     if not st:
#         break;
#     for x in st:
#         if x.islower():
#             low +=1
#         elif x.isupper():
#             up += 1
#         elif x.isnumeric():
#             num += 1
#         elif x.isspace():
#             spa += 1
#
#     print(low, up, num, spa)


while True:
    # 소문자 대문자 숫자 공백
    up = 0
    low = 0
    num = 0
    spa = 0

    st = input()
    if not st:
        break;
    else:
        for x in st:
            if x.islower():
                low +=1
            elif x.isupper():
                up += 1
            elif x.isnumeric():
                num += 1
            elif x.isspace():
                spa += 1

    print(low, up, num, spa)

