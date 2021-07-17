import sys

#정점과 연결선 개수
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

#부모 정점 (초기값 본인으로)
parent = [i for i in range(n+1)]

# 연결선 만들기
lines = [0]*(m)
for i in range(m):
        lines[i] = list(map(int,sys.stdin.readline().split()))

#최소비용순으로 정렬
lines.sort(key = lambda x:x[2])

#최소비용
minCost = 0

#부모찾기 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

#연결함수
def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    parent[x] = y

#크루스칼 풀이
#n은 정점갯수 m은 연결선갯수 lines 연결리스트 parent 부모
def cruskal(n,m,lines,parent):
    global minCost
    for v1,v2,cost in lines:
        if find(v1) == find(v2):
            pass
        else:
            union(v1,v2)
            minCost += cost

cruskal(n,m,lines,parent)
print(minCost)
