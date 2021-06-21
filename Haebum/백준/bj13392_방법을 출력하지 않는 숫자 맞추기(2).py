#dp 문제

#재귀방식 풀이쓰면 시간초과로 포문을 이용예정

#탑다운 방식
#값들을 저장해서 똑같은걸 계산할시 시간줄이기


import sys
import math


# 숫자나사 개수 , 현재상태, 원하는상태
n = int(sys.stdin.readline())
now = sys.stdin.readline()
want = sys.stdin.readline()

# 계산값 저장하기위한 2차원리스트
# 최대 9번까지 돌 수 있음(10번시 원상태)
# 나사개수 최대 10000개
dp = [[-1]*10 for _ in range(10001)]
result = math.inf
lcnt = 0
for i in range(n):
    for j in range(10):
        
        
        int_now = int(now[i])
        int_want = int(want[i])
        int_now += lcnt
        #left 회전
        sub = int_now - int_want
        sub %= 10
        if sub<0:
            sub+=10
        lcnt += sub
        lcnt %= 10
        dp[i][j] = sub+dp[i-1][j]

        if i == n-1:
            result = min(result,dp[i][j])