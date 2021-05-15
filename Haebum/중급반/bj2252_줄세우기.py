from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    print(cur)
    for i in range(len(graph[cur])):
        next = graph[cur][i]
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
        

#시간복잡도...
#32001

#공간복잡도..