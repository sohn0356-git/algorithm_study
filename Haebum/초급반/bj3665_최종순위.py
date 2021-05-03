import sys
from collections import deque

tc = int(sys.stdin.readline())
for i in range(tc):
    n = int(sys.stdin.readline())
    graph = [[]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)
    answer = []
    last_year = list(map(int,sys.stdin.readline().split()))
    newRanking = int(sys.stdin.readline())
    for _ in range(newRanking):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    
    queue = deque()

    for _ in last_year:
        if indegree[_] == 0:
            queue.append(_)

    while queue:
        cur = queue.popleft()
        answer.append(cur)

        for _ in range(len(graph[cur])):
            next = graph[cur][_]
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
    
    if len(answer) != n:
        print("IMPOSSIBLE")
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