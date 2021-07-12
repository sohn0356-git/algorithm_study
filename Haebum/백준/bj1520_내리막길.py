import sys
from collections import deque

# dp를 이용한 풀이
# bfs를 이용하여 해당 좌표에서 4방향 체크
# visited를 별도로 만들어 방문 여부 체크
# 최종 도착시 answer +1 씩 증가


#세로, 가로 높이 칸수
m, n = map(int,sys.stdin.readline().split())

#지도 생성
graph = [0]*m
for i in range(m):
    graph[i] = list(map(int,sys.stdin.readline().split()))

#방법의 수
visited = [[0]*n for _ in range(m)]

que = deque()
que.appendleft([0,0,visited])

dirR = [0,1,0,-1]
dirC = [1,0,-1,0]
answer = 0
while que:
    height, width, visited = que.popleft()
    for i in range(4):
        newHeight = height + dirR[i]
        newWidth = width + dirC[i]
        if 0<= newHeight < m and 0 <= newWidth < n:
            if visited[newHeight][newWidth] == 0 and graph[height][width] > graph[newHeight][newWidth]:
                if newHeight == m-1 and newWidth == n-1:
                    answer +=1
                else:
                    visited[newHeight][newWidth] = 1
                    que.append([newHeight,newWidth,visited])
print(answer)