# 투포인터 풀이
# 스타트랑 앤드를 지정하여 앤드까지 합 계산
# 부족하다면 앤드를 올리고
# 넘는다면 스타트를 올림
# 스타트를 최대치까지 올린 후 정답 리스트에 넣기

import sys

# n 수열의 길이 s 합의 기준
# 10 <= n <= 100,000
# 0 < s <= 100,000,000
n,s = map(int,sys.stdin.readline().split())

#수열
nlist = list(map(int,sys.stdin.readline().split()))

#투포인터
start = 0
end = 0

#합계
sumNum = nlist[0]

#정답
answer = sys.maxsize
flags = 0

while start < n:
    if sumNum < s:
        end += 1
        if end == n:
            break
        sumNum += nlist[end]
    else:
        flags = 1
        answer = min(answer,end-start+1)
        sumNum -= nlist[start]
        start += 1

if flags == 0:
    print(0)
else:
    print(answer)

