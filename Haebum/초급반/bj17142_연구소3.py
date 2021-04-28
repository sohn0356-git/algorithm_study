#문제풀이
# 시간제한 10^8/4
# 바이러스들의 좌표를 리스트에 담아두고 그중에서 m개를 뽑는 리스트를 만든다..
# 50*50 맵에서 최대 나올 수 있는 바이러스는 2500개.. 에서 m의 최대는 10이므로 2500^10 시간복잡도 문제됨..
# 다른방법이 안떠오름 응용해서 풀겠음
# n과 m 방식으로 바이러스 리스트에서 m개를 고르는 재귀함수를 만들고 m개 골라졌을 시 deque를 돌림
# visited에 바이러스가 전염되는 시간을 저장하여 최종 시간 출력 예정


#추가
#파이썬 combination 함수 사용 (n과 m 대신)

from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

n,m = map(int,sys.stdin.readline().split())

graph = [0]*n
v = []
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
for row in range(n):
    graph[row] = list(map(int,sys.stdin.readline().split()))

for columns in range(n):
    for rows in range(n):
        if graph[columns][rows] == 2:
            v.append([columns,rows])

startV = list(combinations(v,m))
answer = -1

def bfs(start,graph):
    visited = [[-1]*n for _ in range(n)]
    graph = deepcopy(graph) # 내용 복사한 새로운 그래프 생성
    queue = deque()

    #extend는 배열을 넣을때 사용(그냥 쓰면 우측으로 붙고 left쓰면 왼쪽으로)
    queue.append(start)

    while queue:
        cur = queue.popleft()
        visited[cur[0]][cur[1]] = 0
        for i in range(4):
            y = cur[0] + dirs[i][0]
            x = cur[1] + dirs[i][1]
            if 0<= x < n and 0<= y < n and visited[y][x] == -1 and graph[y][x] == 0:
                visited[y][x] = visited[cur[0]][cur[1]] +1
                graph[y][x] = 2
                queue.append([y,x])
        
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 0:
                return -1
            else:
                return visited[y][x]
    
for value in startV:
    result = bfs(value,graph)
    if result > answer:
        answer = result

print(answer)


