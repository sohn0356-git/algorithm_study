import sys
from collections import defaultdict
from heapq import *
import math

#행성의 갯수
n = int(sys.stdin.readline())

#방문여부
visited = [0] *(n+1)

#행성담기
star_coordinates = defaultdict()

#행성좌표담기
for i in range(1,n+1):
    x,y,z = map(int,sys.stdin.readline().split())
    star_coordinates[i] = [x,y,z]

firstCost = math.inf
adjacent_star = []

#최소비용
minCost = 0

#시작값의 최소값 구하기
for idx in range(2,n):
    starA = star_coordinates[1]
    starB = star_coordinates[idx]
    cost = min(abs(starA[0]-starB[0]),abs(starA[1]-starB[1]),abs(starA[2]-starB[2]))
    if cost<firstCost:
        firstCost = cost
        adjacent_star = [[firstCost,1,idx]]

heapify(adjacent_star)
visited[1] = 1

while adjacent_star and sum(visited) != n:
    cost,star1,star2 = heappop(adjacent_star)
    adjacent_star = list()
    if visited[star2] == 0:
        visited[star2] = 1
        minCost += cost

        for i in range(1,n):
            if visited[i] == 0:
                starA = star_coordinates[star2]
                starB = star_coordinates[i]
                cost = min(abs(starA[0]-starB[0]),abs(starA[1]-starB[1]),abs(starA[2]-starB[2]))
                heappush(adjacent_star,[cost,star2,i])

print(minCost)
