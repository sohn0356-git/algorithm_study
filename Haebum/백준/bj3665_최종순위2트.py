#순위는 위상정렬!

import sys
from collections import deque

def sort():
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        if graph[a][b]:
            graph[a][b] = False
            indegree[b] -= 1
            graph[b][a] = True
            indegree[a] += 1
        else:
            graph[b][a] = False
            indegree[a] -= 1
            graph[a][b] = True
            indegree[b] += 1

def topological():
    que = deque()

    result = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            que.append(i)
    
    for _ in range(n):
        if len(que) == 0:
            return "IMPOSSIBLE"
        cur = que.popleft()
        result.append(cur)
        for next in range(len(graph[cur])):
            indegree[next] -= 1
            if indegree[next] == 0:
                que.append(next)
                if len(que) == 2:
                    return "?"
    return result

#테스트케이스
t = int(sys.stdin.readline())

for i in range(t):
    #팀의 수
    n = int(sys.stdin.readline())

    #작년 순위(인접차수)
    lastYear = [0] + list(map(int,sys.stdin.readline().split()))

    #바뀐 수
    m = int(sys.stdin.readline())

    #인접차수
    indegree = [0] *(n+1)

    #바뀐거 저장
    graph = [[0]*(n+1) for _ in range(n+1)]
    
    #순위에 따른 저장 5등은 <- 1,2,3,4 인접차수 4
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            graph[lastYear[a]][lastYear[b]] = True
            indegree[lastYear[b]] += 1

    #바뀐 순위 정렬
    sort()

    #순위 정렬
    result = topological()
    
    if result == "IMPOSSIBLE":
        print(result)
    elif result == "?":
        print(result)
    else:
        for rank in result:
            print(rank,end=" ")
        print()
