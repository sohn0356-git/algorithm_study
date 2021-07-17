import sys
from heapq import *
from collections import defaultdict

# V 정점의 개수 E 간선의 개수

#크루스칼의 알고리즘의 경우
# ElogE
#프림 알고리즘의 경우
# 행렬을 사용하면 V² 힙을 사용하면 ElogV


# v 정점의 개수 e 간선의 개수
v, e = map(int,sys.stdin.readline().split())

#그래프 딕셔너리
checkLine = defaultdict(list)

#정점 방문 여부
visited = [0]*(v+1)

# 무방향 그래프 생성
for i in range(e):
    v1,v2,weight = map(int,sys.stdin.readline().split())
    checkLine[v1].append([weight,v1,v2])
    checkLine[v2].append([weight,v2,v1])

# 시작지점 넣기
visited[1] = 1
adjacent_line = checkLine[1]
heapify(adjacent_line)
total_weight = 0

# 우선순위 큐 계속 돌기
while adjacent_line:
    weight,v1,v2 = heappop(adjacent_line) #최소 가중치 뽑기

    if visited[v2] == 0: #방문한적이 없다면
        visited[v2] = 1 #방문한걸로 처리
        total_weight += weight #가중치 더하기

        #연결된 간선 체크
        for line in checkLine[v2]:
            if visited[line[2]] == 0: #연결된 간선 중 방문한게 아니면
                #우선순위큐에 넣기
                heappush(adjacent_line,line)

print(total_weight)