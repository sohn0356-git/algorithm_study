import sys

#이분탐색으로 나무 자르는 길이를 줄이거나 늘리면서 확인


# n 나무 수 m 가져갈 나무 길이
n,m = map(int,sys.stdin.readline().split())
#나무 리스트
trees = list(map(int,sys.stdin.readline().split()))

trees.sort()

start = 0 #나무길이의 최소
end = trees[-1] #나무길이의 최대

#정답
answer =0

def binary(start,end):
    while start<=end:
        mid = (start+end) // 2
        count = 0
        for i in trees:
            if i > mid:
                count += i-mid
        
        # 자른 길이가 가져갈 길이보다 길거나 같다면
        # 톱날 높이 증가
        if count >= m:
            global answer
            start = mid+1
            answer = mid
        else:
            end = mid-1

binary(start,end)
print(answer)