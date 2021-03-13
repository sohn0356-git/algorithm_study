#1부터 N까지 자연수 중에서 M개를 고른 수열
#같은 수를 여러 번 골라도 된다

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
        used[stage] = i
        solve(stage+1) ##여기서 재귀

solve(0)
