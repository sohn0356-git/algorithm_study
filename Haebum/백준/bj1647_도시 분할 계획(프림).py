import sys
from collections import defaultdict, deque
from heapq import *

#프림 풀이
#마을이 두개인데 마을간의 연결도로는 지울 수 있으므로
#마지막에 들어올 최대 유지비를 다른 마을로 두어서
# 마지막 유지비값을 제외하면 된다


#n은 집 m은 길
n , m = map(int,sys.stdin.readline().split())

#길 딕셔너리
adjacent_lines = defaultdict(list)

for i in range(m):
    home1, home2, cost = map(int,sys.stdin.readline().split())
    adjacent_lines[home1].append([cost,home1,home2])
    adjacent_lines[home2].append([cost,home2,home1])

#방문여부체크
visited = [0]* (n+1)

#초기값 설정
adjacent_road = adjacent_lines[1]
heapify(adjacent_road)
visited[1] = 1

#최소 유지비
minCost = 0

#마지막 저장값
temp = 0

while adjacent_road:
    cost, home1, home2 = heappop(adjacent_road)
    if visited[home2] == 0: #방문하지 않았다면
        visited[home2] = 1
        minCost += cost
        temp = cost #마지막 값 저장
        adjacent_road.clear()
        for road in adjacent_lines[home2]:
            if visited[road[2]] == 0:
                heappush(adjacent_road,road)

print(minCost-temp)
