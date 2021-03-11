from collections import deque

n,m,v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

visited_dfs =[0]*(n+1)
visited_bfs = [0]*(n+1)

for _ in range(m):
    s, e = map(int,input().split())
    graph[s][e] = 1
    graph[e][s] = 1

def dfs(node):
    print(node,end=" ")
    visited_dfs[node] = 1
    for i in range(1,n+1):
        if graph[node][i] and visited_dfs[i]==0:
            dfs(i)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited_bfs[node] = 1

    while queue:
        cur = queue.popleft()
        print(cur,end= " ")

        for i in range(1,n+1):
            if graph[cur][i] and visited_bfs[i]==0:
                queue.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)