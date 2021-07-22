# 최소시간과 최대시간을 설정해두고
# 이분탐색으로 시간을 줄여 나가기

import sys

# n은 심사대 갯수 m은 총인원
n, m = map(int,sys.stdin.readline().split())

#심사대 심사시간 리스트
immigration = []
for _ in range(n):
    time = int(sys.stdin.readline())
    immigration.append(time)

#정렬
immigration.sort()

#초기값
start = 1
end = immigration[-1] *m

#정답
answer = 0

def binary(start,end):
    while start<= end:
        mid = (start+end)//2
        count = 0
        #그시간대에 몇명이 통과할수 있는지 인원수 확인
        for i in immigration:
            num = mid // i
            count += num
        #인원 적으면 시간증가
        if count < m:
            start = mid +1
        #인원 많으면 시간감소
        else:
            global answer
            end = mid -1
            answer = mid


binary(start,end)
print(answer)