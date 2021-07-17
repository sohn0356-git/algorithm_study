# 실패! dp문제 쉬운문제였지만 생각을 못했따..

import sys

n = int(sys.stdin.readline())
rgb = []

for i in range(n):
    rgb.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,len(rgb)):
    rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0],rgb[i-1][1]) + rgb[i][2]
answer = min(rgb[n-1][0],rgb[n-1][1],rgb[n-1][2])

print(answer)