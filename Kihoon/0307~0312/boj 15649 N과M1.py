#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

N, M = map(int, input().split())

used = [0]*M
visited = [0]*N
card = []

for i in range(1,N+1):
    card.append(i)

def solve(stage): #재귀함수
    if stage==M:
        for i in used:
            print(card[i], end=' ')
        print()
        #print(used)
        return

    for i in range(N):
        if visited[i]==0:
            visited[i] = 1
            used[stage] = i
            solve(stage+1) ##여기서 재귀
            visited[i] = 0

solve(0)
