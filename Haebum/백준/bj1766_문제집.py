# 위상정렬로 순서 정렬

import sys
from heapq import *

#문제의 수 n 정보의개수 m
n,m = map(int,sys.stdin.readline().split())

#순서도
graph = [[] for _ in range(n+1)]

#인접차수
indegree = [0]*(n+1)

# 순서도 채우기
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

# 큐 생성
que = []
heapify(que)

#시작노드 집어넣기
for i in range(1,n+1):
    if indegree[i] == 0:
        heappush(que,i)

#우선순위큐 기준으로 출력
while que:
    cur = heappop(que)
    print(cur, end= " ")
    for j in range(len(graph[cur])):
        next = graph[cur][j]
        indegree[next] -=1
        if indegree[next] == 0:
            heappush(que,next)
