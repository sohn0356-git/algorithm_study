import sys
from collections import defaultdict
from heapq import *

#프림 풀이
#풀이의 핵심은 연결비용을 전부 구할려고하면 안된다
#x,y,z좌표별로 정렬하여 인접값만 구해서 넣을것!

#행성의 갯수
n = int(sys.stdin.readline())

#방문여부
visited = [0] *(n+1)

#행성좌표담기
xList = []
yList = []
zList = []
for i in range(1,n+1):
    x,y,z = map(int,sys.stdin.readline().split())
    xList.append([x,i])
    yList.append([y,i])
    zList.append([z,i])

#좌표정렬
xList.sort()
yList.sort()
zList.sort()

#행성별 연결리스트담기
tunnels = defaultdict(list)

for i in range(1,n):
    xCost = abs(xList[i-1][0]-xList[i][0])
    xStar1 = xList[i-1][1]
    xStar2 = xList[i][1]
    yCost = abs(yList[i-1][0]-yList[i][0])
    yStar1 = yList[i-1][1]
    yStar2 = yList[i][1]
    zCost = abs(zList[i-1][0]-zList[i][0])
    zStar1 = zList[i-1][1]
    zStar2 = zList[i][1]
    tunnels[xStar1].append([xCost,xStar1,xStar2])
    tunnels[xStar2].append([xCost,xStar2,xStar1])
    tunnels[yStar1].append([yCost,yStar1,yStar2])
    tunnels[yStar2].append([yCost,yStar2,yStar1])
    tunnels[zStar1].append([zCost,zStar1,zStar2])
    tunnels[zStar2].append([zCost,zStar2,zStar1])

#최소비용
minCost = 0

#초기값 설정
adjacent_star = tunnels[1]
heapify(adjacent_star)
visited[1] = 1

# 큐 돌기
while adjacent_star:
    cost,star1,star2 = heappop(adjacent_star)
    if visited[star2] == 0: #방문하지 않았다면(연결되지 않았다면)
        visited[star2] = 1 #방문한것으로 표시
        minCost += cost

        for tunnel in tunnels[star2]: #star2를 기준으로 방문여부확인
            if visited[tunnel[2]] == 0:
                heappush(adjacent_star,tunnel)

print(minCost)
