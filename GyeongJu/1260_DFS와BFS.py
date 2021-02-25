from collections import deque

N, M ,start = map(int,input().split(' '))
arrList = [[0]*(N+1) for i in range(N+1)]
visited = [0]*(N+1)
queue = deque()

for e in range(M):
    e1, e2 = map(int,input().split(' '))
    arrList[e1][e2] = 1
    arrList[e2][e1] = 1



def dfs(start):
    global arrList, N, M, visited
    visited[start] = 1
    print(start, end=' ')
    for i in range(1,N+1):
        if visited[i]==0 and arrList[start][i]==1:
            dfs(i)

dfs(start)
visited = [0]*(N+1)
print()
queue.appendleft(start)
visited[start] = 1
while len(queue) != 0:
    cur = queue.pop()
    print(cur, end=' ')
    for i in range(1,N+1):
        if visited[i] == 0 and arrList[cur][i] == 1:
            queue.appendleft(i)
            visited[i] = 1