# 구글링 해서 답지 봄... ㅠ

#1번 풀이
#dfs를 이용한 풀이
#일을 하냐 안하냐를 통해 풀기(퇴사일이 종료조건)
#시간복잡도는 2^15
#공간복잡도는 4byte*15*2 *15?

n = int(input()) #퇴사일-1

t,p = [0]*(n+1), [0]*(n+1) # 상담기간, 이익

for idx in range(1,n+1): #상담기간 이익 리스트에 담기
    t[idx],p[idx] = map(int,input().split())

answer = 0 #정답

def dfs(i,sum):
    if i==n+1: #퇴사일이면
        global answer
        answer = max(answer,sum) #현재 총이익과 기존 정답과 비교하여 큰것을 정답에 담기
        return #종료

    if i + t[i] <= n+1: #일을했을때 상담끝나는기간이 퇴사일과 같거나 작을경우
        dfs(i+t[i],sum+p[i]) #상담끝나는기간, 총이익+상담이익을 담아 dfs돌리기

    if i+1 <= n+1: #일을 안했을때
        dfs(i+1,sum) #다음날과 현재 총이익 담아서 dfs돌리기

dfs(1,0) #상담첫날, 현재 총이익은 0 담아서 돌리기
print(answer)


#2번 문제 풀이
#dp를 이용한 풀이
#마지막부터 처음으로 돌아오며, 상담이 가능하냐 안하냐를 따져서 푼다.
#가능할경우엔 맡았을때와 맡지않았을때의 이익을 비교해서 처리
#시간복잡도 15*2..?

N = int(input())
work_pay = [] #상담날짜와 이익을 리스트로 한번에 저장
max_pay = [0] * N

for _ in range(N):
    work_pay.append(list(map(int, input().split()))) #저장부분
   
for i in range(N-1, -1, -1): #뒤에서부터  다이나믹 프로그래밍
    day = work_pay[i][0] #상담날짜
    pay = work_pay[i][1] #이익
    
    if day > N - i: #남은 기간보다 상담일이 길 경우
        if i != N-1:  #i가 상담 마지막날이 아니라면?
            max_pay[i] = max_pay[i+1] #이전 최댓값 저장
        continue
        
    if i == N-1: #마지막 날 하루짜리 상담
        max_pay[i] = pay #
    elif i + day == N: #현재 일을 시작하면 정확히 마지막에 끝나는 경우
        max_pay[i] = max(pay, max_pay[i+1])
    else:
        #현재 일을 맡을 경우 or 맡지 않을 경우
        max_pay[i] = max(pay + max_pay[i + day], max_pay[i+1])

print(max_pay[0])


#3번 문제 풀이
#dp를 이용해서 풀지만 첫날부터 마지막으로
n = int(input())

t, p = [0]*n, [0]*n

for i in range(n):
    t[i], p[i] = map(int, input().split())
        
dp = [0]*25

for i in range(n):
    if dp[i] > dp[i+1]: # 현재가 다음날보다 보상이 높다면
        dp[i+1] = dp[i] # 다음날 보상은 현재로
    if dp[i+t[i]] < dp[i] + p[i]: # T일 후에 받게될 금액이 현재의 보상보다 높다면
        dp[i+t[i]] = dp[i] + p[i] # T일후에 보상을 넣는다.
        
print(dp[n])