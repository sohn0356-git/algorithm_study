M, N = map(int, input().split())
route = []
visited = [[0] * N for _ in range(M)]
for _ in range(M):
    route.append(list(map(int, input().split())))
answer = 0
vecX = [-1, 0, 1, 0]
vecY = [0, 1, 0, -1]

# DFS 풀이 -> 시간초과
def solution(route, M, N, x, y):
    global answer, vecX, vecY
    if x == N-1 and y == M-1:
        answer += 1
        return
    else:
        for i in range(4):
            nextX, nextY = x+vecX[i], y+vecY[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                if visited[nextY][nextX] == 0 and route[nextY][nextX] < route[y][x]:
                    visited[nextY][nextX] = 1
                    solution(route, M, N, nextX, nextY)
                    visited[nextY][nextX] = 0

visited[0][0] = 1
solution(route, M, N, 0, 0)
print(answer)