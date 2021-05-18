#조건
# 3잔 연속 못마심
# 가장 많이 마신 포도주 양

import sys

n = int(sys.stdin.readline())
wine = [-1]*(n+1)

for i in range(n):
    wine[i] = int(sys.stdin.readline())

