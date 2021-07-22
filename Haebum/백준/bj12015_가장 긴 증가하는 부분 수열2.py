#길이를 기준으로 start,end 설정
# # 이분탐색으로 체크

import sys

# n 수열크기 a 수열의 원소집합
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

#크기 순 정렬       
a.sort()
start = 1
end = n

#정답
answer = 0

def binary(start,end):
    while start<= end:
        mid = (start+end) //2

        count = 0
        temp = a[0]
        for i in range(1,n-1):
            





  
