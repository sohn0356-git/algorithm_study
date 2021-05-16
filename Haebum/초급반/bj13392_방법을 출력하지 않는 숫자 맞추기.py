#dp 문제

#재귀방식 풀이지만 파이썬은 재귀에 약함
#같은코드로 c사용시 통과 파이썬은 시간초과 뜸

#바텀업 방식
#solve(현재자리,왼쪽으로 돌린 횟수)를 불러올거임
#값들을 저장해서 똑같은걸 계산할시 시간줄이기


import sys
#너무 많은 재귀를 돌지 않기위한 조건설정
sys.setrecursionlimit(100000)


# 숫자나사 개수 , 현재상태, 원하는상태
n = int(sys.stdin.readline())
now = sys.stdin.readline()
want = sys.stdin.readline()

# 계산값 저장하기위한 2차원리스트
# 최대 9번까지 돌 수 있음(10번시 원상태)
# 나사개수 최대 10000개
dp = [[-1]*10 for _ in range(10001)]


def solve(stage,leftTurn):
    global dp,now,want
    #현재 나사개수 넘을 시 0으로
    if stage == n:
        return 0

    #계산한 값이 있으면 그걸 바로 불러옴
    if dp[stage][leftTurn] != -1:
        return dp[stage][leftTurn]

    #현재 나사의 위치숫자와 원하는 숫자 가져오기
    int_now = int(now[stage])
    int_want = int(want[stage])

    #현재까지 왼쪽으로 돌린 숫자만큼 더해줌    
    int_now += leftTurn
    #10일시 원상태(한바퀴돔)이므로 10으로 나눠줌
    int_now %= 10

    #turn left
    #왼쪽으로 돌리면 1씩 증가! ex) 3(now)->4(want)로 가기 위해선 4(want)-3(now) =1번돌리면 됨
    sub = int_want - int_now #sub=돌린 횟수
    if sub<0: #음수이면
        #+10을 하기 ex) 9(now) -> 2(want) :  0 1 2 = 3  수식 2 - 9 = -7 +10 = 3
        sub += 10 
    # 정답 = 현재 왼쪽으로 돌린 횟수(sub) + 그다음 값의 최소 돌린횟수(solve) 
    t1 = sub + solve(stage+1,(leftTurn+sub)%10)

    #turn right
    sub - int_now - int_want #오른쪽은 -1 왼쪽과 반대로
    if sub<0:
        sub += 10
    # 정답 = 현재 오른쪽으로 돌린 횟수(sub) + 그다음 값의 최소 돌린횟수(solve)
    t2 = sub + solve(stage+1,leftTurn)

    #최소정답 = 왼쪽과 오른쪽으로 돌린것중에 제일 작은 값
    res = min(t1,t2)
    return res



    #turn right



print(solve(0,0))