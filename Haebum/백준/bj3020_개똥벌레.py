#높이를 기준으로 이분탐색

import sys

#길이 n 높이 m
n,m = map(int,sys.stdin.readline().split())


caveRow = [] # 석순
caveHigh = [] # 종유석

for i in range(n):
    obstacle = int(sys.stdin.readline())
    if i%2 ==0:
        caveHigh.append(obstacle)
    else:
        caveRow.append(obstacle)

caveRow.sort()
caveHigh.sort()


def binary(array,height):
    #장애물의 어느높이부터 부딪히는지 확인하기 위한 이분탐색
    #start end는 장애물 높이를 구하기위한 자리값
    #고로 index 0 ~ (len(array)-1)
    #mid는 중간높이의 장애물 index값
    # 중간높이의 장애물(array[mid])과 height가 마주치지 않는다면
    # 장애물의 높이를 높여 부딪히는지 확인
    #  중간높이의 장애물(array[mid])과 height가 마주친다면
    # 장애물의 높이를 낮춰서 어디서부터 부딪히는지 확인
    
    start,end = 0, len(array)-1
    while start<= end:

        mid = (start+end) //2
        
        if array[mid] < height:
            start = mid+1
        else:
            end = mid-1
    
    return start

#정답
minHigh = n
minCnt = 0

#for문을 돌며 현재 높이 체크
for i in range(1,m+1):
    down = len(caveRow) - binary(caveRow,i-0.5)
    top = len(caveHigh) - binary(caveHigh,m-i+0.5)

    if minHigh == down + top:
        minCnt +=1
    elif minHigh > down +top:
        minHigh = down+top
        minCnt = 1

print(minHigh,minCnt)
    