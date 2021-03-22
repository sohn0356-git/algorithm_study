from collections import deque
MAX = 100000
MIN = 0

def bfs(N):
    cnt = 0;
    visited[N] = 1;
    queue = deque([[N, cnt]])

    while queue:
        cur, cnt = queue.popleft();
        if cur == M:
            return cnt

        else:
            cnt += 1;
            if (cur * A) <= MAX and not visited[cur * A]:
                queue.append([cur * A, cnt])
                visited[cur * A] = 1;
            if (cur + A) <= MAX and not visited[cur + A]:
                queue.append([cur + A, cnt])
                visited[cur + A] = 1;
            if (cur - A) >= MIN and not visited[cur - A]:
                queue.append([cur - A, cnt])
                visited[cur - A] = 1;

            if (cur * B) <= MAX and not visited[cur * B]:
                queue.append([cur * B, cnt])
                visited[cur * B] = 1;
            if (cur + B) <= MAX and not visited[cur + B]:
                queue.append([cur + B, cnt])
                visited[cur + B] = 1;
            if (cur - B) >= MIN and not visited[cur - B]:
                queue.append([cur - B, cnt])
                visited[cur - B] = 1;

            if (cur + 1) <= MAX and not visited[cur + 1]:
                queue.append([cur + 1, cnt])
                visited[cur + 1] = 1;
            if (cur - 1) >= MIN and not visited[cur - 1]:
                queue.append([cur - 1, cnt])
                visited[cur - 1] = 1;
    return cnt

A,B,N,M = map(int, input().split(' '));

visited = [0]*(MAX - MIN + 1)
print(bfs(N))
