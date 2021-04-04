# 토마토 - 재도전..

from collections import deque;

def count():
    global tomatoes, spos;
    cnt = 0;
    dx = [-1, 0, 1, 0];
    dy = [0, 1, 0, -1];
    queue = deque();
    for _ in spos:
        y, x = _;
        queue.append([y, x, 0]);
        visited[y][x] = 0;
    while queue:
        y, x, c = queue.popleft();
        for i in range(4):
            yy = y + dy[i];
            xx = x + dx[i];
            if 0 <= yy < N and 0 <= xx < M:
                if visited[yy][xx] == -1 and tomatoes[yy][xx] == 0:
                    visited[yy][xx] = c + 1;
                    tomatoes[yy][xx] = 1;
                    queue.append([yy, xx, c + 1]);
                    if cnt < visited[yy][xx]:
                        cnt = visited[yy][xx];
    return cnt;


M, N = map(int, input().split());
tomatoes = [];
spos = [];
visited = [[-1] * M for _ in range(N)];
for n in range(N):
    temp = list(map(int, input().split()));
    tomatoes.append(temp);
    if 1 in temp:
        for m in range(M):
            if temp[m] == 1:
                spos.append([n, m]);
chk = False;
cnt = count();
for _ in range(N):
    if 0 in tomatoes[_]:
        chk = True;
if chk:
    print(-1);
else:
    print(cnt);