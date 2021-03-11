# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
#
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
#
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.
# (1, 1)과 (N, M)은 항상 0이라고 가정하자.
#
# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

from collections import deque;

def move(start_y, start_x):
    global S, visited;
    queue = deque([[start_y, start_x, 0]]);
    visited[start_y][start_x] = 1;
    while queue:
        y, x, one = queue.popleft();
        if (y, x) == (N - 1, M - 1) and one <= 1:
            return visited[y][x];
        if y + 1 < N and not visited[y + 1][x]:
            if one < 1:
                visited[y + 1][x] = visited[y][x] + 1;
                if S[y + 1][x] == 1:
                    queue.append([y + 1, x, one + 1]);
                else:
                    queue.append([y + 1, x, one]);
            else:
                if S[y + 1][x] != 1:
                    visited[y + 1][x] = visited[y][x] + 1;
                    queue.append([y + 1, x, one]);
        if y - 1 >= 0 and not visited[y - 1][x]:
            if one < 1:
                visited[y - 1][x] = visited[y][x] + 1;
                if S[y - 1][x] == 1:
                    queue.append([y - 1, x, one + 1]);
                else:
                    queue.append([y - 1, x, one]);
            else:
                if S[y - 1][x] != 1:
                    visited[y - 1][x] = visited[y][x] + 1;
                    queue.append([y - 1, x, one]);
        if x + 1 < M and not visited[y][x + 1]:
            if one < 1:
                visited[y][x + 1] = visited[y][x] + 1;
                if S[y][x + 1] == 1:
                    queue.append([y, x + 1, one + 1]);
                else:
                    queue.append([y, x + 1, one]);
            else:
                if S[y][x + 1] != 1:
                    visited[y][x + 1] = visited[y][x] + 1;
                    queue.append([y, x + 1, one]);
        if x - 1 >= 0 and not visited[y][x - 1]:
            if one < 1:
                visited[y][x - 1] = visited[y][x] + 1;
                if S[y][x - 1] == 1:
                    queue.append([y, x - 1, one + 1]);
                else:
                    queue.append([y, x - 1, one]);
            else:
                if S[y][x - 1] != 1:
                    visited[y][x - 1] = visited[y][x] + 1;
                    queue.append([y, x - 1, one]);



N, M = map(int, input().split());
S=[];
visited = [[0] * M for _ in range(N)];
for i in range(N):
    str = input();
    temp = [];
    for j in str:
        temp.append(int(j));
    S.append(temp);
# print(S);
# print(visited);

x=0; y=0;
result = move(y, x)
if result:
    print(result);
else:
    print(-1);

###반례###
# 8 8
# 00000000
# 11111001
# 00000001
# 00111110
# 10111110
# 10011000
# 11111000
# 00000000