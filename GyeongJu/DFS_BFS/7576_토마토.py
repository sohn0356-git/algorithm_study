from collections import deque

M, N = map(int, input().split(' '))
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for i in range(N)]
queue = deque()

dirR = [0,1,0,-1]
dirC = [1,0,-1,0]

for i in range(N):
    for j in range(M):
        if farm[i][j]==1:
            queue.appendleft((i,j))
            visited[i][j] = 0

while queue:
    cur = queue.pop()
    for d in range(4):
        nI = cur[0]+dirR[d]
        nJ = cur[1]+dirC[d]
        if nI>=0 and nI<N and nJ>=0 and nJ<M:
            if visited[nI][nJ]==-1 and farm[nI][nJ]==0:
                farm[nI][nJ]=1
                visited[nI][nJ] = visited[cur[0]][cur[1]] + 1
                queue.appendleft((nI,nJ))

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]==-1 and farm[i][j]==0:
            ans=-1
            break
        if ans < visited[i][j]:
            ans = visited[i][j]
    if ans==-1:
        break

print(ans)