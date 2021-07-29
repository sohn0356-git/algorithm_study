# 위상정렬로 순서정리

import sys
from collections import deque

# 테스트케이스 숫자
t = int(sys.stdin.readline())

for _ in range(t):
    # n 건물의 수 k 건물건설 순서규칙
    n, k = map(int,sys.stdin.readline().split())
    # 연결도
    graph = [[] for _ in range(n+1)]
    # 인접차수
    indegree = [0]*(n+1)
    # 각 건물 완성까지 걸린 시간
    buildingTime = [0]*(n+1)
    # 짓는 시간
    timeList = [0] + list(map(int,sys.stdin.readline().split()))

    #순서도 채우기 및 인접차수 증가
    for _ in range(k):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    
    #지으면 이기는 건물
    win = int(sys.stdin.readline())
    #큐 생성
    que = deque()

    # #시작노드 넣기
    for node in range(len(indegree)):
        if indegree[node] == 0:
            que.append(node)
            buildingTime[node] = timeList[node]
    

    #큐를 돌면서 순서대로 정렬
    while que:
        node = que.popleft()
        # 노드와 연결된 건물체크
        for building in range(len(graph[node])):
            #다음 순서의 건물
            next = graph[node][building]
            #각 건물 완성까지 걸린 시간
            buildingTime[next] = max(buildingTime[next],buildingTime[node]+timeList[next])
            # 다음 순서의 건물 -1
            indegree[next] -=1
            if indegree[next] == 0:
                que.append(next)

    print(buildingTime[win])


