# 문제
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을
# 작성하시오.
#
#
#
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는
# 사각형이다.
#
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는
# 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의
# 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
#
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
#
# 입력의 마지막 줄에는 0이 두 개 주어진다.
# from collections import deque
#
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
# while True:
#     w, h = map(int, input().split(' '))
#     if w == 0 and h == 0:
#         break;
#     map_s = [list(map(int,input().split(' '))) for _ in range(h)]
#     q = deque()
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if map_s[i][j] == 1:
#                 q.append((i, j))
#                 map_s[i][j] = 2
#                 while q:
#                     cx, cy = q.popleft()
#                     for k in range(8):
#                         nx = cx + dx[k]
#                         ny = cy + dy[k]
#                         if 0 <= nx < h and 0 <= ny < w:
#                             if map_s[nx][ny] == 1:
#                                 q.append((nx, ny))
#                                 map_s[nx][ny] = 2
#                 else:
#                     cnt += 1
#
#
#     print(cnt)



from collections import deque

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def bfs(island):
    global dx, dy
    cnt = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            # 땅이면
            # bfs 탐색
            if island[i][j] == 1:
                island[i][j] = 2
                q.append((i,j))

                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        cx = x + dx[k]
                        cy = y + dy[k]
                        if 0 <= cx < h and 0 <= cy < w:
                            if island[cx][cy] == 1:
                                 island[cx][cy] = 2
                                 q.append((cx, cy))
                cnt += 1
    print(cnt)


while True:
    w, h = map(int, input().split(' '))
    if w == 0 and w == 0:
        break
    island = [list(map(int, input().split(' '))) for _ in range(h)]

    bfs(island)


