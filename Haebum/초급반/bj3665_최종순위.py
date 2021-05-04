import sys
from collections import deque

def topological():
    queue = deque()

    #진입차수 0 -> queue 삽입
    for _ in range(1,n+1):
        if indegree[_] == 0:
            queue.append(i)

    #위상정렬
    answer = []

    while queue:
        cur = queue.popleft()
        answer.append(cur)

        for _ in range(len(graph[cur])):
            next = graph[cur][_]
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
                if len(queue) >=2:
                    return "?"

    return answer


tc = int(sys.stdin.readline())

for i in range(tc):
    n = int(sys.stdin.readline())
    graph = [[False]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)
    last_year = list(map(int,sys.stdin.readline().split()))
    newRanking = int(sys.stdin.readline())

    #작년결과를 토대로 설정 
    for x in range(n):
        for y in range(i+1,n):
            graph[last_year[x]][last_year[y]] = True
            indegree[last_year[y]] += 1

    #순위변동
    for _ in range(newRanking):
        a,b = map(int,sys.stdin.readline().split())
        if not graph[a][b]:
            graph[b][a] = False
            indegree[b] += 1
            graph[a][b] = True
            indegree[a] -= 1
        else:
            graph[b][a] = True
            indegree[b] -= 1
            graph[a][b] = False
            indegree[a] += 1

    
    answer = topological()

    if len(answer) != n:
        print("IMPOSSIBLE")
    elif answer == "?":
        print(answer)
    elif newRanking==0:
        for _ in last_year:
            print(_,end=" ")
        print()
    elif answer == last_year:
        print("IMPOSSIBLE")
    else:
        for _ in answer:
            print(_,end=" ")
        print()