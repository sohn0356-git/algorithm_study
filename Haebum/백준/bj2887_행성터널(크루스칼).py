import sys
from collections import defaultdict

#크루스칼 풀이
# def find(x):
#     if x == parent[x]:
#         return x
    
#     parent[x] = find(parent[x])
#     return parent[x]

# def union(x,y):
#     x = parent[x]
#     y = parent[y]

#     if x==y:
#         return

#     parent[x] = y


# #행성의 갯수
# n = int(sys.stdin.readline())

# #부모정점 생성
# parent = [i for i in range(n)]

# #행성담기
# star_coordinates = defaultdict(list)


# #행성좌표담기
# for i in range(1,n+1):
#     coordinates = list(map(int,sys.stdin.readline().split()))
#     star_coordinates[i].append(coordinates)

# starLine = [0] *(n+1)

# #행성최소비용연결 담기
# for i in range(1,n):
#     starA = star_coordinates[i]
#     starB = star_coordinates[i+1]
#     starLine[i] = [i,i+1,min(abs(starA[0]-starB[0]),abs(starA[1],starB[1]),abs(starA[2],starB[2]))]

# #행성최소비용으로 정렬
# starLine.sort()

