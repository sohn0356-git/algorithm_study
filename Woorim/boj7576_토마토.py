# bfs
# 깊이를 구하는 문제 (가장 깊은 bfs의 깊이 = 토마토가 다익는 최소 날짜)
# 중요!!!!! 큐에 값을 push 하는 시점 - 처음에 초기화 할 때
#                                                   --> 그래야 한번에 같은 depth를 탐색할 수 있다.
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(tomato, N, M, q):
    global dx, dy
    while q:
        i, j = q.popleft()
        for k in range(4):
            cx = i + dx[k]
            cy = j + dy[k]
            # 이동한 좌표값이 상자의 영역 한에 포함되면
            if 0 <= cx < N and 0 <= cy < M:
                # 익지 않은 토마토면 값을 부모토마토값만큼 더하고 큐에 푸시
                if tomato[cx][cy] == 0:
                    tomato[cx][cy] = tomato[i][j] + 1
                    q.append((cx, cy))

    return tomato



M, N = map(int, input().split(' '))
tomato = [[0]*M]*N
for i in range(N):
    tomato[i] = list(map(int, input().split(' ')))
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))

result = bfs(tomato, N, M, q)
max = 1
for i in range(N):
    for j in range(M):
        if result[i][j] == 0:
            max = -1
        else:
            if result[i][j] > max:
                max = result[i][j]
        if max == -1:
            break
    if max == -1:
        break

if max == -1:
    print(max)
else:
    print(max-1)

