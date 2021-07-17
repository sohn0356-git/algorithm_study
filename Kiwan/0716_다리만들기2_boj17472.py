import sys
from collections import deque

N, M = list(map(int,sys.stdin.readline().rstrip().split()))
info = []
for i in range(N):
    info.append(list(map(int,sys.stdin.readline().rstrip().split())))

vecx = [-1, 0, 1, 0]
vecy = [0, 1, 0, -1]
# 섬 번호
idx = 0
# 섬 좌표를 갖고 있는 딕셔너리를 만든다
island = dict()
visited = [[0] * M for _ in range(N)]

# 섬과 섬 그리고 2이상의 가중치

for j in range(N):
    for i in range(M):
        q = deque()
        if info[j][i] == 0:
            continue
        else:
            if visited[j][i] == 0:
                visited[j][i] = 1
                q.append((i,j))
                idx += 1
                info[j][i] = idx
                if island.get(idx) == None:
                    island[idx] = [(i,j)]
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + vecx[k], y + vecy[k]
                    if 0 <= nx < M and 0 <= ny < N:
                        if info[ny][nx] == 1 and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            info[ny][nx] = idx
                            q.append((nx,ny))
                            island[idx].append((nx,ny))

# for idx in island:
#     island[idx].sort(key = lambda x : (x[0], x[1]))
#     print(island[idx])
# for item in info:
#     print(item)
# print(island)
graph = set()
for idx in island:
    for coordxy in island[idx]:
        x, y = coordxy
        for k in range(4):
            nx, ny = x + vecx[k], y + vecy[k]
            weight = 0
            while True:
                if 0 <= nx < M and 0 <= ny < N:
                    if info[ny][nx] == 0:
                        weight += 1
                        nx += vecx[k]
                        ny += vecy[k]
                    else:
                        if info[ny][nx] != info[y][x]:
                            if weight != 1:
                                graph.add((weight, info[y][x], info[ny][nx]))
                        break
                else:
                    break

def Find(x, parent):
    if x == parent[x]:
        return x
    else:
        parent[x] = Find(parent[x], parent)
        return parent[x]

def Union(x, y, parent, weight):
    global weightSum
    xx, yy = x, y
    x = Find(x, parent)
    y = Find(y, parent)

    if x == y:
        return

    parent[x] = y
    weightSum += weight
    check.add((weight,xx,yy))

graph = list(graph)
parent = dict()
check = set()
graph.sort(key = lambda x : (x[0], x[1]))
weightSum = 0

for elem in graph:
    weight, x, y = elem
    if weight == 1:
        continue
    else:
        if parent.get(x) == None:
            parent[x] = x
        if parent.get(y) == None:
            parent[y] = y

        Union(x, y, parent, weight)

# if weightSum != 0:
if len(check) == idx - 1:
    print(weightSum)
else:
    print(-1)

print(graph)
print(check)
for item in info:
    print(item)




