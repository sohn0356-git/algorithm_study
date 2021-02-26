from collections import deque

N, K = map(int,input().split(' '))

MAX_SIZE = 200001
visited = [-1]*MAX_SIZE

queue = deque()
queue.appendleft(N)
visited[N] = 0

while queue:
    cur = queue.pop()
    if cur==K:
        print(visited[cur])
        break
    if cur-1>=0 and visited[cur-1]==-1:
        visited[cur-1]=visited[cur]+1
        queue.appendleft(cur-1)

    if cur+1<MAX_SIZE and visited[cur+1]==-1:
        visited[cur+1]=visited[cur]+1
        queue.appendleft(cur+1)

    if cur*2<MAX_SIZE and visited[cur*2]==-1:
        visited[cur*2]=visited[cur]+1
        queue.appendleft(cur*2)