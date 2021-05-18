# n <=1000

#dp
import sys

n = int(sys.stdin.readline())
dp = [0] *(n+1)
dp[1] = 1
dp[2] = 2
answer = 0
for i in range(3,n+1):
    dp[i] = dp[i-1]%10007 + (dp[i-2])%10007

if n == 1:
    print(1)
elif n==2:
    print(2)
else:
    print(dp[n]%10007)