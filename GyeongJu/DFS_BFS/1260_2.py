from collections import deque

N, M, start = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

visited = [0] * (N+1)

# def dfs(node):
#     global N, graph
#     visited[node] = 1
#     print(node, end=' ')
#     for i in range(1, N+1):
#         if graph[node][i] == 1 and visited[i] == 0:
#             dfs(i)

# dfs(start)
# print()
# visited = [0] * (N+1)

# # 1번
# visited = [-1] * (N+1)
# queue = deque()
# queue.append(start)
# visited[start] = 0

# while queue:
#     cur = queue.popleft()
#     # print(cur, end=' ')
    

#     for i in range(1, N+1):
#         if graph[cur][i] == 1 and visited[i] == -1:
#             queue.append(i)
#             visited[i] = visited[cur] + 1
# print(visited[1:])

# # 2번
# queue = deque()
# queue.append((3,0))
# visited[start] = 1

# while queue:
#     cur = queue.popleft()   # (node, depth)
#     # print(cur, end=' ')
#     print(cur, end=' ')

#     for i in range(1, N+1):
#         if graph[cur[0]][i] == 1 and visited[i] == 0:
#             queue.append((i, cur[1] + 1))
#             visited[i] = 1
