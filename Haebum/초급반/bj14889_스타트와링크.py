# 4<=N<=20 N은 짝수

n = int(input())
card ={}
for i in range(n):  #N개의 줄에 N개로 이루어진 수 입력
    card[i] = list(map(int,input().split()))


start = [0]*int(n/2) #기존의 used이고 start팀 멤버
visited = [0]*n
answer = []
def solve(stage):
    global answer
    if stage==n/2:
        link = []
        linkScore = 0
        startScore = 0
        for i in range(n):
            link.append(i)
        for i in start:
            link.remove(i)
            for j in start:
                if i!=j:
                   startScore += card[i][j]
        for i in link:
            for j in link:
                if i!=j:
                    linkScore += card[i][j] 
        balance = abs(startScore - linkScore)
        if not answer:
            answer.append(balance)
        elif balance < answer[0]:
            answer[0] = balance
        return

    for i in range(n):
        if stage>0 and start[stage-1]> i: #오름차순 정렬
                continue
        if visited[i] == 0:
            visited[i] = 1
            start[stage] = i
            solve(stage+1)
            visited[i] = 0

solve(0)
print(answer[0])

#시간복잡도.. (2*10)**10