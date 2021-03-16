# https://www.acmicpc.net/problem/2206
# 입력: 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
# 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
# 출력: 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

from collections import deque

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def bfs():
    queue = deque([(0, 0, 1, False)])
    visited[0][0][0] = True
    while queue:
        x, y, count, remove = queue.popleft()
        if x == M - 1 and y == N - 1:
            return count
        else:
            for index in range(4):
                j = x + dc[index]
                i = y + dr[index]
                if 0 <= j < M and 0 <= i < N:
                    if not remove and not visited[i][j][0]:
                        # 벽 안부수고
                        if gameMap[i][j] == '0':
                            queue.append([j, i, count + 1, False])
                            visited[i][j][0] = True
                        else:
                            queue.append([j, i, count + 1, True])
                            visited[i][j][1] = True
                    elif remove and not visited[i][j][1] and gameMap[i][j] == '0':
                        # 벽을 이미 부쉈을떄
                        queue.append([j, i, count + 1, True])
                        visited[i][j][1] = True
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    gameMap = []
    for _ in range(N):
        gameMap.append(list(input()))
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]  # visited[N][M][2]
    print(bfs())