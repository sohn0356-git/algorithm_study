# 정렬되어있는 두 배열 a,b
# 두배열 합친 다음 정렬해서 출력할것

# 배열당 크기 10^6
# 투포인터로 쓸것

import sys
n,m = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
c = []
left = 0
right = 0

while True:
    if left >= len(a):
        c += b[right:]
        break
    elif right >= len(b):
        c += a[left:]
        break
    elif a[left] <= b[right]:
        c.append(a[left])
        left +=1
    else:
        c.append(b[right])
        right +=1

for i in c:
    print(i,end=" ")