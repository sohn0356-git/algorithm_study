# 투포인터로 품
# 정렬을 해두고

import sys
# n 수열의 길이 m 차이 기준
n, m = map(int,sys.stdin.readline().split())

nlist = []
for i in range(n):
    nlist.append(int(sys.stdin.readline()))

#정렬
nlist.sort()

start = 0
end = 0

#최대값 지정
answer = sys.maxsize

while True:
    if start >= n or end >= n:
        break
    if abs(nlist[start]-nlist[end]) < m:
        end+=1
    elif abs(nlist[start]-nlist[end]) == m:
        answer = abs(nlist[start]-nlist[end])
        break
    else:
        answer = min(answer,abs(nlist[start]-nlist[end]))
        start +=1

print(answer)
