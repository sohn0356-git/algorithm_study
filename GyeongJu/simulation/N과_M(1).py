N, M = map(int, input().split())

used = [0]*M
visited = [0]*N
card = []

for i in range(1,N+1):
    card.append(i)

def solve(stage):
    if stage==M:
        for i in used:
            print(card[i], end=' ')
        print()
        return

    for i in range(N):
        if visited[i]==0:
            visited[i] = 1
            used[stage] = i
            solve(stage+1)
            visited[i] = 0

solve(0)