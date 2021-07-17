import sys
from collections import defaultdict

#크루스칼 풀이
#풀이의 핵심은 연결비용을 전부 구할려고하면 안된다
#x,y,z좌표별로 정렬하여 인접값만 구해서 넣을것!
# 1  2  3  4  5
# 11 14 -1 10 19 x좌표
#  3  4  1  2  5 n-1개*3개
# -1 10 11 14 19 정렬

# -15 -5 -1 -4 -4 y좌표
#  3  4  5   2  1 
#  -1  -4 -4 -5 -15 정렬

# (1 -2 3),(2 1 10),(2 5 5),()

# x,y,z좌표를 정렬을 해서
#간선을 만든다


#부모노드 찾기
def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

#두개 연결시키기
def union(x,y):
    x = parent[x]
    y = parent[y]

    if x==y:
        return

    parent[x] = y


#행성의 갯수
n = int(sys.stdin.readline())

#부모정점 생성
parent = [i for i in range(n+1)]

# #행성의 좌표를 x,y,z 별도로 받기
xList = []
yList = []
zList = []

#행성좌표별로 담기
for i in range(1,n+1):
    x,y,z = list(map(int,sys.stdin.readline().split()))
    xList.append([x,i])
    yList.append([y,i])
    zList.append([z,i])

#좌표별 정렬
xList.sort()
yList.sort()
zList.sort()

#최소비용 연결리스트
starLine = list()

# #행성최소비용연결 담기
for i in range(1,n):
    starLine.append([xList[i-1][0]-abs(xList[i][0]),xList[i-1][1],xList[i][1]])
    starLine.append([abs(yList[i][0]-yList[i-1][0]),yList[i-1][1],yList[i][1]])
    starLine.append([abs(zList[i][0]-zList[i-1][0]),zList[i-1][1],zList[i][1]])
    
#행성최소비용으로 정렬
starLine.sort()

#최소비용
minCost = 0

#최소비용으로 정렬된 연결리스트 돌기
for i in starLine:
    cost = i[0]
    star1 = i[1]
    star2 = i[2]
    #안이어져있다면 이어주기
    if find(star1) != find(star2):
        union(star1,star2)
        minCost+= cost

print(minCost)

