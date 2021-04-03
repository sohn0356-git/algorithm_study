import sys

p, n = map(int,input().split())
v = list(map(int,input().split()))
answer = 0
divnum = 1000000007
for i in range(n):
    answer += v[i] %divnum
    if i == n-1:
        break
    answer *= p %divnum

print(answer%divnum)