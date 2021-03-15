from collections import deque

A, B, N, M = map(int, input().split())

stone = [-1]*100001

queue = deque()
stone[N] = 0
queue.append(N)

while queue:
    cur = queue.popleft()
    if cur == M:
        print(stone[M])
        break
    if cur - 1 >= 0 and stone[cur-1]==-1:
        stone[cur-1] = stone[cur]+1
        queue.append(cur-1)

    if cur - A >= 0 and stone[cur-A]==-1:
        stone[cur-A] = stone[cur]+1
        queue.append(cur-A)

    if cur - B >= 0 and stone[cur-B]==-1:
        stone[cur-B] = stone[cur]+1
        queue.append(cur-B)

    if cur + 1 <= 100000 and stone[cur+1]==-1:
        stone[cur+1] = stone[cur]+1
        queue.append(cur+1)
    
    if cur + A <= 100000 and stone[cur+A]==-1:
        stone[cur+A] = stone[cur]+1
        queue.append(cur+A)

    if cur + B <= 100000 and stone[cur+B]==-1:
        stone[cur+B] = stone[cur]+1
        queue.append(cur+B)
    
    if cur * A <= 100000 and stone[cur*A]==-1:
        stone[cur*A] = stone[cur]+1
        queue.append(cur*A)

    if cur * B <= 100000 and stone[cur*B]==-1:
        stone[cur*B] = stone[cur]+1
        queue.append(cur*B)
