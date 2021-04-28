import heapq

V, E = map(int, input().split())
start = int(input())
distances = [987564321]*(V+1)
visited = [-1]*(V+1)
graph = [[] for _ in range(V+1)]

for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])

distances[start] = 0

queue = []

heapq.heappush(queue, [distances[start],start])

while queue:
    dist, cur = heapq.heappop(queue)

    if visited[cur]!=-1:
        continue

    visited[cur] = 1

    for next in graph[cur]:
        distance = dist + next[1]
        if distance < distances[next[0]]:
            distances[next[0]] = distance
            heapqq.heappush(queue, [distance, next[0]])

