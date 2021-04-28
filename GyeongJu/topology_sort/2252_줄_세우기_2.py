from collections import deque

N, M = map(int, input().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

queue = deque()

for i in range(1,N+1):
    if indegree[i]==0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    print(cur, end=' ')

    for next in graph[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
