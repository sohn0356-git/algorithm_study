import heapq
import collections
import sys

N = int(sys.stdin.readline()) # 노드 수
M = int(sys.stdin.readline()) # 간선 수
graph = collections.defaultdict(list) # 빈 그래프 생성
visited = [0] * (N+1) # 노드 방문정보 초기화

# 무방향 그래프 생성
for i in range(M):
    u,v,weight = list(map(int,sys.stdin.readline().rstrip().split()))
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

# print(graph)

def prim(graph, start_node):
    visited[start_node] = 1
    edges = graph[start_node]
    heapq.heapify(edges)
    mst = []
    total_weight = 0

    while edges:
        weight,u,v = heapq.heappop(edges)

        if visited[v] == 0:
            visited[v] = 1
            mst.append((u,v))
            total_weight += weight

            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(edges, edge)

    return total_weight

print(prim(graph, 1))