import sys

# 크루스칼을 통한 풀이

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

# n 집의개수 m 길의 개수
n, m = map(int,sys.stdin.readline().split())

#부모리스트 생성
parent = [i for i in range(n+1)]


#길 리스트 생성 및 코스트 기준 넣기
adjacent_lines = []

for i in range(m):
    home1, home2, cost = map(int,sys.stdin.readline().split())
    adjacent_lines.append([cost,home1,home2])

#코스트기준 정렬
adjacent_lines.sort()

#최소 유지비
minCost = 0

#마지막 값 저장 변수
temp = 0

for cost,home1,home2 in adjacent_lines:
    if find(home1) != find(home2):
        union(home1,home2)
        minCost += cost
        temp = cost

minCost -= temp
print(minCost)
