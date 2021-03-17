from collections import deque

n,m = map(int,input().split())

graph= [[] for _ in range(n+1)]
inDegree = [0]*(n+1)
queue = deque()

for i in range(m):
    a,b = map(int,input().split())
    graph[a] = graph.append(b)
    inDegree[b] += 1

for i in range(1,n+1):
    if inDegree[i]==0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    print(cur,end=" ")

    for i in range(1,n+1):
        if graph[cur][i] > 0:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                queue.append(i)

        

#시간복잡도...
#32001

#공간복잡도..
