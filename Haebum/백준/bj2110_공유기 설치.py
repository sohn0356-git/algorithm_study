import sys

# 이분탐색 풀이
# 좌표를 기준으로 공유기 간 최대거리를 구하여
# 거리에 몇개를 설치 가능한지 여부를 체크
# 최대거리를 줄이거나 늘려서 확인

n,c = map(int,sys.stdin.readline().split())

home = []
for i in range(n):
    home.append(int(sys.stdin.readline()))

#좌표 정렬
home.sort()


#초기 스타트 앤드 좌표
start = 1 #나올 수 있는 최소의 거리
end = home[-1] - home[0] #나올 수 있는 최대의 거리

#정답
answer =0 

def binary(start,end):
    while start<=end:
        # 공유기 사이의 최대거리
        distance = (start+end) // 2
        
        #현재 좌표
        current = home[0]
        #공유기 설치 수
        count = 1
        for i in range(1,len(home)):
            #현재 집의 좌표가 공유기 사이의 최대거리보다 멀거나 같다면
            if home[i] >= current + distance:
                count +=1 #공유기 설치
                current = home[i] #현재 좌표를 공유기 설치집으로 이동

        # 공유기 설치 개수가 많거나 같다면
        if c <= count:
            global answer
            #최대거리를 더 멀리
            start = distance +1
            answer = distance
        #적다면
        else:
            #최대거리를 더 적게
            end = distance -1
    
    return

binary(start,end)
print(answer)