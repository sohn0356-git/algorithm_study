# 문제
# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
# (한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
# (0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)
#
#   1	1	0	0	0	0	0	0	0	0
#   0	1	0	0	0	0	0	0	0	0
#   0	0	0	0	1	0	0	0	0	0
#   0	0	0	0	1	0	0	0	0	0
#   0	0	1	1	0	0	0	1	1	1
#   0	0	0	0	1	0	0	1	1	1
#
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
#
# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

from collections import deque

def findWarm(pos, visited, M, N):
    count = 0;
    queue = deque([]);
    for i in range(N):
        for j in range(M):
            subcount = 0;
            if visited[i][j]:
                continue;
            else:
                # if i == 3 and j == 8:
                #     print();
                queue.append([j, i]);
                if pos[i][j] == 1:
                    subcount += 1;
                while queue:
                    x, y = queue.popleft();
                    # if y == 4 and x == 7:
                    #     print();
                    if not visited[y][x]:
                        visited[y][x] = True;
                    if x+1 < M and not visited[y][x+1]:
                        visited[y][x+1] = True;
                        if pos[y][x+1] == 1:
                            queue.append([x+1,y]);
                            subcount += 1;
                    if x-1 >= 0 and not visited[y][x-1]:
                        visited[y][x-1] = True;
                        if pos[y][x-1] == 1:
                            queue.append([x-1,y]);
                            subcount += 1;
                    if y-1 >= 0 and not visited[y-1][x]:
                        visited[y-1][x] = True;
                        if pos[y-1][x] == 1:
                            queue.append([x,y-1]);
                            subcount += 1;
                    if y+1 < N and not visited[y+1][x]:
                        visited[y+1][x] = True;
                        if pos[y+1][x] == 1:
                            queue.append([x,y+1]);
                            subcount += 1;
                if subcount > 0:
                    count += 1;
    return count;

T = int(input());
ans = [];
for tc in range(T):
    M, N, K = map(int, input().split());
    xyArr = [];
    pos = [];
    visited = [];

    for i in range(K):
        [x, y] = map(int, input().split());
        xyArr.append([x, y]);

    for i in range(N):
        pos.append([]);
        visited.append([]);
        for j in range(M):
            visited[i].append(False);
            if [j, i] in xyArr:
                pos[i].append(1);
            else:
                pos[i].append(0);
    ans.append(findWarm(pos, visited, M, N));
for i in ans:
    print(i);

from collections import deque

##되는 코드 ..왜?..
# def findWarm(pos, visited, M, N):
#     count = 0;
#     queue = deque([]);
#     for i in range(N):
#         for j in range(M):
#             subcount = 0;
#             if visited[i][j]:
#                 continue;
#             else:
#                 if pos[i][j] == 1:
#                     queue.append([j, i]);
#                     visited[i][j] = True;
#                     subcount += 1;
#                 while queue:
#                     x, y = queue.popleft();
#                     if x + 1 < M and not visited[y][x + 1]:
#
#                         if pos[y][x + 1] == 1:
#                             visited[y][x + 1] = True;
#                             queue.append([x + 1, y]);
#                             subcount += 1;
#                     if x - 1 >= 0 and not visited[y][x - 1]:
#
#                         if pos[y][x - 1] == 1:
#                             visited[y][x - 1] = True;
#                             queue.append([x - 1, y]);
#                             subcount += 1;
#                     if y - 1 >= 0 and not visited[y - 1][x]:
#
#                         if pos[y - 1][x] == 1:
#                             visited[y - 1][x] = True;
#                             queue.append([x, y - 1]);
#                             subcount += 1;
#                     if y + 1 < N and not visited[y + 1][x]:
#
#                         if pos[y + 1][x] == 1:
#                             visited[y + 1][x] = True;
#                             queue.append([x, y + 1]);
#                             subcount += 1;
#                 if subcount > 0:
#                     count += 1;
#     return count;
#
#
# T = int(input());
# ans = [];
# for tc in range(T):
#     M, N, K = map(int, input().split());
#     xyArr = [];
#     pos = [];
#     visited = [];
#
#     for i in range(K):
#         [x, y] = map(int, input().split());
#         xyArr.append([x, y]);
#
#     for i in range(N):
#         pos.append([]);
#         visited.append([]);
#         for j in range(M):
#             visited[i].append(False);
#             if [j, i] in xyArr:
#                 pos[i].append(1);
#             else:
#                 pos[i].append(0);
#     ans.append(findWarm(pos, visited, M, N));
# for i in ans:
#     print(i);