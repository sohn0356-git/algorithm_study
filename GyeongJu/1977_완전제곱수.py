from math import sqrt

N = int(input())
M = int(input())

num = []

for i in range(N,M+1):
    if int(sqrt(i)) == sqrt(i):
        num.append(i)

if len(num)==0:
    print(-1)
else:
    print(sum(num))
    print(num[0])