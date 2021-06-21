from collections import deque

n,k = map(int,input().split())
visited = [-1]*200001

queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    cur = queue.popleft()

    if cur == k:
        print(visited[k])
        break
    
    if (cur-1) >=0 and visited[cur-1] == -1:
        visited[cur-1] = visited[cur] +1
        queue.append(cur-1)

    if (cur+1) <=200000 and visited[cur+1] == -1:
        visited[cur+1] = visited[cur] +1
        queue.append(cur+1)

    if (cur*2) <=200000 and visited[cur*2] == -1:
        visited[cur*2] = visited[cur] +1
        queue.append(cur*2)