
ans = 0
N,M = map(int, input().split(' '))
card = list(map(int, input().split(' ')))

used = [0]*3
visited = [0]*N

def solve(stage):
    global ans, N, M, visited, used
    if stage==3:
        sum = 0
        for i in used:
            sum += card[i]
        if sum <= M and ans < sum:
            ans = sum        
        return

    for i in range(N):
        if visited[i]==0:
            visited[i] = 1
            used[stage] = i
            solve(stage+1)
            visited[i] = 0

solve(0)
print(ans)