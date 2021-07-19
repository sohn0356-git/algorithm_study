import sys
import math

# 공유기 시작과 끝에 설치
# 남은 공유기 개수로 시작과 끝 좌표의 중간에 가장 가까운 집에 공유기 설치
# 공유기집의 좌표를 기준으로 절반마다 설치?

n,c = map(int,sys.stdin.readline().split())

home = []
modem = []
for i in range(n):
    home.append(int(sys.stdin.readline()))

#좌표 정렬
home.sort()

#공유기 설치 여부 체크
visited = [0] *(n+1)

#첫 공유기 갯수 체크
modemNum = c

#초기 스타트 앤드
start = home[0]
end = home[-1]
c -= 2
visited[0] = 1
visited[-1] = 1
modem.append(home[0])
modem.append(home[-1])


def binary(c,start,end):
    #공유기 다 설치
    if c == 0:
        return
    #공유기를 설치할 중간값
    mid = (start+end) // 2
    answer = math.inf
    #공유기 설치할 집 번호
    modemSetting = 0
    
    #홈을 돌면서
    for idx,i in enumerate(home):
        if visited[idx] == 0: #설치하지 않았다면
            if answer > abs(mid-i): #중간값에서 제일 가까운가?
                answer = abs(mid-i)
                modemSetting = idx
    visited[modemSetting] = 1 #설치한것으로 체크
    c -= 1 #공유기갯수 줄이기
    modem.append(home[modemSetting]) #공유기 설치 집 좌표 넣기
    #설치한 좌표값을 기준으로 두개의 binary 돌리기
    binary(c,start,home[modemSetting])
    binary(c,home[modemSetting],end)

def maxLength():
    answer = 0
    modem.sort()
    for i in range(1,len(modem)-1):
        temp = min(abs(modem[i]-modem[i-1]),abs(modem[i]+modem[i+1]))
        if temp > answer:
            answer = temp
    return answer


binary(c,start,end)
#초기 공유기가 2개일때 처리
if modemNum == 2:
    print(abs(home[0]-home[-1]))
else:
    answer = maxLength()
    print(answer)
