import sys
sys.setrecursionlimit(10**6)
def Find(x, parent):
    if parent[x] == x:
        return x
    else:        
        parent[x] = Find(parent[x], parent)
        return parent[x]

def Union(x, y, parent):
    x = Find(x, parent)
    y = Find(y, parent)
    if x != y:
        parent[x] = y

def dfs(r, c):
    global visited, island_num, island, N, M
    visited[r][c] = island_num
    for d in range(4):
        nR = r + dirR[d]
        nC = c + dirC[d]
        if nR>=0 and nR<N and nC>=0 and nC<M:
            if island[nR][nC]==1 and visited[nR][nC]==0:
                dfs(nR,nC)

def check(parent):
    global island_num
    for i in range(1,island_num):
        if Find(i,parent) != Find(i+1,parent):
            return False
    return True

def build(sum, r, c, parent):
    global answer
    if check(parent):
        if answer == -1 or answer > sum:
            answer = sum
        return
    for i in range(r,N):
        for j in range(M):
            if visited[i][j] != 0:
                for d in range(4):
                    nI = i + dirR[d]
                    nJ = j + dirC[d]
                    if nI >= 0 and nI < N and nJ >= 0 and nJ < M:
                        if visited[nI][nJ] == 0:
                            length = 0
                            while visited[nI][nJ] == 0:
                                nI = nI + dirR[d]
                                nJ = nJ + dirC[d]
                                if nI >= 0 and nI < N and nJ >= 0 and nJ < M:
                                    length += 1
                                else:
                                    length = 0
                                    break
                            if length >= 2 and visited[nI][nJ]!=visited[i][j]:
                                x = Find(visited[i][j], parent)
                                y = Find(visited[nI][nJ], parent)
                                if x != y:
                                    newParent = [0]*7
                                    for p in range(7):
                                        newParent[p] = parent[p]
                                    newParent[x] = y
                                    build(sum+length, i, j,newParent)

N, M = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dirR = [0,1,0,-1]
dirC = [1,0,-1,0]
parent = []
answer = -1
island_num = 0
# print(island)

for i in range(7):
    parent.append(i)

for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and visited[i][j] == 0:
            island_num += 1
            dfs(i,j)

build(0,0,0,parent)
print(answer)
                    



