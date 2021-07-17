import sys

# dp를 이용한 풀이
# dfs를 이용한 탑다운 풀이

def DFS(i, j):
    if not i and not j:
        return 1
    if (i < 0 or i >= n or j < 0 or j >= m):
        return 0
    if memoization[i][j] != -1:
        return memoization[i][j]
    
    memoization[i][j] = 0
 
    for way in range(4):
        ii = i + dx[way]
        jj = j + dy[way]
 
        if ii < 0 or ii >= n or jj < 0 or jj >= m:
            continue
        
        if graph[ii][jj] > graph[i][j]:
            memoization[i][j] += DFS(ii, jj)
 
    return memoization[i][j]
#세로, 가로 높이 칸수
n, m = map(int,sys.stdin.readline().split())

#지도 생성
graph = [0]*m
for i in range(n):
    graph[i] = list(map(int,sys.stdin.readline().split()))

memoization = [[-1] * m for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
print(DFS(n-1,m-1))
