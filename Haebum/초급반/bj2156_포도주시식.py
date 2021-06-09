#조건
# 3잔 연속 못마심
# 가장 많이 마신 포도주 양
# dp문제

import sys

n = int(sys.stdin.readline())
dp = [-1]*(n+1)
wine = []
for i in range(n):
    wine.append(int(sys.stdin.readline()))

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
#dp[2] = max((wine[0]+wine[1]), (wine[0]+wine[2]), (wine[1]+wine[2]))
dp[2] = max(dp[1],dp[0]+wine[2],wine[1]+wine[2])
#dp[3] = max(wine[0]+wine[2]+wine[3],wine[1]+wine[2],wine[0]+wine[1]+wine[3])
# dp[3] = max(dp[0]+wine[2]+wine[3],dp[2],dp[1]+wine[3])
# #dp[4] = max(wine[0]+wine[1]+ wine[3]+wine[4],wine[0]+wine[2]+wine[3],wine[1]+wine[2] +wine[4])
# dp[4] = max(dp[1]+wine[3]+wine[4],dp[3],dp[2]+wine[4])

for i in range(3,n):
    dp[i] = max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])

print(dp[n-1])