# n 의 갯수 3~10000(10^4)

# dp 문제로 추정됨
# n의 갯수와 초기상태를 알려줌

import sys

n = int(sys.stdin.readline())
first = map(int,sys.stdin.readline().split(""))
final = map(int,sys.stdin.readline().split(""))


for i in range(n):
    for j in range(9):
        dp[i][j] = min(dp[i][j],dp[i][j-1] + rcnt)

def left(digit,first):
    for _ in range(digit,len(first)):
        first[_] += 1
    return first


def right(digit,first):
    first[digit] -= 1
    return first