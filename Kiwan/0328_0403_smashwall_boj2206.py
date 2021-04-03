# # 벽 부수고 이동하기
#
from collections import deque;

def bfs(lev):
    global visited1, visited2, mapp, N, M, vec;
    queue = deque([[0, 0, 0, lev + 1]]);
    visited[0][0][0] = lev + 1;
    visited[0][0][1] = lev + 1;
    while queue:
        posy, posx, smash, lev = queue.popleft();
        if posy == N - 1 and posx == M - 1:
            return lev;
        for y, x in vec:
            posy += y; posx += x;
            if posy >= 0 and posx >= 0 and posy < N and posx < M:
                if smash == 0:
                    if visited[posy][posx][0] == 0:
                        if mapp[posy][posx] == 0:
                            queue.append([posy, posx, 0, lev + 1]);
                            visited[posy][posx][0] = lev + 1;
                            posy -= y; posx -= x;
                        else:
                            queue.append([posy, posx, 1, lev + 1]);
                            visited[posy][posx][1] = lev + 1;
                            posy -= y; posx -= x;
                    else:
                        posy -= y; posx -= x;
                        continue;
                else:
                    if visited[posy][posx][1] == 0:
                        if mapp[posy][posx] == 0:
                            queue.append([posy, posx, 1, lev + 1]);
                            visited[posy][posx][1] = lev + 1;
                            posy -= y; posx -= x;
                        else:
                            posy -= y; posx -= x;
                            continue;
                    else:
                        posy -= y; posx -= x;
                        continue;
            else:
                posy -= y; posx -= x;
                continue;
    return -1;

N, M = map(int, input().split());
vec = [[1, 0], [0, 1], [-1, 0], [0, -1]];
mapp = [];
visited = [[[0, 0] for _ in range(M)] for _ in range(N)];
for _ in range(N):
    temp = input();
    mapp.append(list(map(int, temp)));

print(bfs(0));

# from collections import deque
#
# dr = (0, 1, 0, -1)
# dc = (1, 0, -1, 0)
#
# def bfs():
#     queue = deque([(0, 0, 1, False)])
#     visited[0][0][0] = True
#     while queue:
#         x, y, count, remove = queue.popleft()
#         if x == M - 1 and y == N - 1:
#             return count
#         else:
#             for index in range(4):
#                 j = x + dc[index]
#                 i = y + dr[index]
#                 if 0 <= j < M and 0 <= i < N:
#                     if not remove and not visited[i][j][0]:
#                         # 벽 안부수고
#                         if gameMap[i][j] == '0':
#                             queue.append([j, i, count + 1, False])
#                             visited[i][j][0] = True
#                         else:
#                             queue.append([j, i, count + 1, True])
#                             visited[i][j][1] = True
#                     elif remove and not visited[i][j][1] and gameMap[i][j] == '0':
#                         # 벽을 이미 부쉈을떄
#                         queue.append([j, i, count + 1, True])
#                         visited[i][j][1] = True
#     return -1
#
#
# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     gameMap = []
#     for _ in range(N):
#         gameMap.append(list(input()))
#     visited = [[[False, False] for _ in range(M)] for _ in range(N)]  # visited[N][M][2]
#     print(bfs())