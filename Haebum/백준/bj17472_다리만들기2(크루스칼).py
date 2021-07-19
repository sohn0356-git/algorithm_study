import sys
from collections import deque

# bfs를 통해 섬을 만들고 간선 뽑기
# 크루스칼을 통해 섬들을 연결하는 최소값 구하기

#조건
# 1<= n,m <= 10
# 3 <= n*m <= 100
# 2 <= 섬의개수 <= 6

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    parent[x] = y

#부모생성
parent = [i for i in range(7)]

#맵의 세로, 가로
n, m = map(int,sys.stdin.readline().split())

#맵 생성
graph = [0]*n

for i in range(n):
    graph[i] = list(map(int,sys.stdin.readline().split()))

#방문여부
visited = [[0]*m for _ in range(n)]

#좌표변동 리스트
dirR = [0,0,-1,1]
dirC = [1,-1,0,0]

#섬생성 que
que = deque()
islandNum = 0

#섬 번호 지정
for height in range(n):
    for witdh in range(m):
        if graph[height][witdh] == 1 and visited[height][witdh] == 0:
            islandNum += 1
            visited[height][witdh] = 1
            graph[height][witdh] = islandNum
            que.append([height,witdh])
        
        while que:
            cur = que.popleft()
            for i in range(4):
                x = cur[0] + dirR[i]
                y = cur[1] + dirC[i]
                if 0 <= x < n and 0 <= y < m:
                    if visited[x][y] == 0 and graph[x][y] !=0:
                        graph[x][y] = islandNum
                        visited[x][y] = 1
                        que.append([x,y])

#각 섬 연결다리 구하기
briges = []
for xx in range(n):
    for yy in range(m):
        if graph[xx][yy] != 0:
            que.append([xx,yy])

        while que:
            cur = que.popleft()
            #가로 고정 세로 방향 이동하며 연결 섬 확인
            for num in range(4):
                length = 0
                idx = 0
                while True:
                    idx +=1
                    x = cur[0] +dirR[num]*idx
                    y = cur[1] +dirC[num]*idx
                    if 0 <= x < n and 0 <= y < m:
                        if graph[x][y] == 0:
                            length +=1
                        elif graph[cur[0]][cur[1]] != graph[x][y]:
                            if length == 1:
                                break
                            briges.append([length,graph[cur[0]][cur[1]],graph[x][y]])
                            break
                        else:
                            break
                    else:
                        break

#연결리스트 정렬
briges.sort()

#최소연결다리길이
minLength = 0

#전체 연결 불가능 확인
check = 0
check2 = set()
for length,island1,island2 in briges:
    if find(island1) != find(island2):
        union(island1,island2)
        check2.add((island1,island2))
        check2.add(island2)
        check += 1
        minLength += length



#섬의개수랑 확인
if len(check2) == islandNum:
    print(minLength)
else:
    print(-1)
