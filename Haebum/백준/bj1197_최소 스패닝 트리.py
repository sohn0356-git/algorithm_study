import sys


# mst 크루스칼 풀이
# union-find를 이용하여 풀이
# 가중치를 기준으로 정렬하여 for문 돌면서 이어져있는지 확인

# 부모 찾기 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

# 부모 연결 함수 (두개가 이어져 있다!)
def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    parent[x] = y

# m 정점의갯수 n 간선의 갯수
m,n = map(int,sys.stdin.readline().split())
parent = [i for i in range(m+1)] #부모리스트 생성 초기값은 본인의 숫자
lines = [0]*n # 간선리스트
answer = 0 #토탈 가중치값

# 간선리스트에 담기
for j in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    lines[j] = line

#가중치 기준으로 정렬
lines.sort(key=lambda x:x[2])

#간선 돌기
for line in lines:
    #이어져있다면 패스
    if find(line[0]) == find(line[1]):
        pass
    # 안이어져있으면
    else:
        union(line[0],line[1]) #유니온으로 이어주기!
        answer += line[2] #가중치는 토탈 가중치에 더해주기

print(answer)
