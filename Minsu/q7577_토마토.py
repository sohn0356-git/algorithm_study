# https://www.acmicpc.net/problem/7576
# 입력: 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다.
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다.
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.
# 출력: 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

from collections import deque

M, N = map(int, input().split());
box = []; # visited
for i in range(0, N):
    box.append(list(map(int, input().split())));

# 시작 정점 입력
# i는 행 j는 열
queue = deque();
for i in range(0, N):
    for j in range(0, M):
        print(box[i][j]);
        if box[i][j] == 1:
            queue.append([i, j, 0]);

def bfs():
    while queue:
        i, j, t = queue.popleft();
        for row in (i - 1, i + 1):
            for col in (j - 1, j + 1):
                if row >= 0 and row < M and col >= N and col < N:
                    if box[row][col] == 0:
                        box[row][col] = 1;
                        queue.append([row, col, t+1]);
    return t;

time = bfs();
count0 = 0;
for i in range(0, M):
    count0 += box[i].count(0);
if count0 > 0:
    print(-1);
else:
    print(time);