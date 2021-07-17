from collections import deque
t = int(input())
dirR = [0,1,0,-1] #상우하좌
dirC = [1,0,-1,0]
for _ in range(t):
    cnt = 0
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            queue = deque()
            if graph[i][j] == 1 and visited[i][j] == 0:
                queue.append([i,j])
                visited[i][j] = 1
                cnt += 1
                while queue:
                    cur = queue.popleft()

                    for k in range(4):
                        x = cur[0] + dirR[k]
                        y = cur[1] + dirC[k]
                        if (0<=x and x<n) and (0<=y and y<m):
                            if graph[x][y] == 1 and visited[x][y]==0:
                                graph[x][y] = 0
                                visited[x][y] = 1
                                queue.append([x,y])

    print(cnt)