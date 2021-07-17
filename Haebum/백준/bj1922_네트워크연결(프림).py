import sys
from collections import defaultdict
from heapq import *

#정점과 연결선 개수
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

#정점 방문여부
visited = [0] *(n+1)

# 연결 그래프 생성
graph = defaultdict(list)

#그래프에 담기
for _ in range(m):
    v1,v2,cost = map(int,sys.stdin.readline().split())
    graph[v1].append([cost,v1,v2])
    graph[v2].append([cost,v2,v1])

#큐 생성 및 초기값 담기
adjacent_line = graph[1]
heapify(adjacent_line)
visited[1] = 1
#최소비용
minCost = 0

# 우선순위큐에 있으면 계속 돌기
while adjacent_line:
    cost,v1,v2 = heappop(adjacent_line) #최소기준으로 하나 뽑기

    if visited[v2] == 0: #연결안되어있으면
        visited[v2] = 1 #연결되어있는걸로 체크
        minCost += cost #비용 더하기

        for line in graph[v2]: #v2 기준으로 연결되어있는것들 확인
            if visited[line[2]] == 0: # 연결안되어있으면
                heappush(adjacent_line,line) #우선순위큐에 추가

print(minCost)


