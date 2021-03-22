from collections import deque
MAX = 100000
MIN = 0

def bfs(N):
    cnt = 0;
    visited[N] = 1;
    queue = deque([[N, cnt]])

    while queue:
        cur, cnt = queue.popleft();
        if cur == K:
            return cnt

        else:
            cnt += 1;
            if (cur * 2) <= MAX and not visited[cur * 2]:
                queue.append([cur * 2, cnt])
                visited[cur * 2] = 1;
            if (cur + 1) <= MAX and not visited[cur + 1]:
                queue.append([cur + 1, cnt])
                visited[cur + 1] = 1;
            if (cur - 1) >= MIN and not visited[cur - 1]:
                queue.append([cur - 1, cnt])
                visited[cur - 1] = 1;
    return cnt

N,K = map(int, input().split(' '));
if N>K:
    print(N-K);
else:
    visited = [0]*(MAX - MIN + 1)
    print(bfs(N))
