import sys


# 레슨의 수 n  블루레이 수 m
n,m = map(int,sys.stdin.readline().split())

#레슨 리스트
lesson = list(map(int,sys.stdin.readline().split()))

start = max(lesson)
end = sum(lesson)

def binary(start,end):
    while start<=end:
        global answer
        mid = (start+end) // 2 # 블루레이 크기
        count = 1 #블루레이 갯수
        blueSum = 0 #블루레이에 현재 담긴 양

        for i in lesson: #레슨 동영상 돌기
            if blueSum + i<= mid: #블루레이에 담을 수 있냐
                blueSum += i
            else: #없다면
                count +=1 #새로운 블루레이 꺼내서 담기
                blueSum = i
        
        if count > m: #지금 블루레이갯수가 지정된 갯수보다 많다면
            start = mid+1 # 블루레이 크기 증가
        else: #적거나 같다면
            end = mid -1 # 블루레이 크기 감소
            answer = mid # 정답에 담기
 
binary(start,end)
print(answer)
