

# deque를 사용해야할 것으로 보임? bfs?
# 해보면서 파악 예정

import sys

# n 밭의 크기 m 나무의 개수 k 최종년수
n,m, k = map(int,sys.stdin.readline().split())
# 밭 설정
graph = [[[] for _ in range(n)] for _ in range(n)]
#초기 양분 설정
A = [[5]*n for _ in range(n)]
#매년 추가할 양분
plus_A = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# 초기 나무 나이 설정
for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    graph[x-1][y-1].append(z)

#방향백터설정
dirC = [0,1,0,-1,-1,1,1,-1]
dirR = [1,0,-1,0,-1,1,-1,1]

#년차수만큼 돌기
for year in range(k):
    # 봄, 여름
    for width in range(n):
        for height in range(n):
            if graph[width][height]: #나무가 있을때
                graph[width][height].sort() #나무들 나이순으로 정렬
                temp_tree, dead_tree = [], 0 #산나무, 죽은나무 구분
                for age in graph[width][height]:
                    if A[width][height] >= age: # 양분이 나무의 나이보다 많을때
                        A[width][height] -= age # 양분에서 나무의 나이만큼 빼고
                        temp_tree.append(age+1) # 산나무 리스트에 +1해서 넣기
                    else:
                        dead_tree += age//2  #죽은나무는 양분으로 변환시켜 넣기
                A[width][height] += dead_tree # 현재양분에 죽은나무양분 넣기
                graph[width][height] = [] # 죽은나무들은 제거해주기위해 없던걸로 초기화한후
                graph[width][height].extend(temp_tree) # 산 나무리스트를 더함
    
    #가을
    print(graph)
    for width in range(n):
        for height in range(n):
            if graph[width][height]:
                for age in graph[width][height]:
                    if age%5 ==0: #나이가 5의 배수일 경우
                        for vec in range(8): #방향백터 돌리기
                            xx = width + dirR[vec]
                            yy = height + dirC[vec]
                            if xx>=0 and xx<n and yy>=0 and yy<n:
                                graph[xx][yy].append(1) # 1살짜리 나무 추가
    
    #겨울
    for width in range(n):
        for height in range(n):
            A[width][height] += plus_A[width][height] #양분 더하기

answer = 0
for width in range(n):
    for height in range(n):
        answer += len(graph[width][height]) #나무의 숫자만큼 더하기

print(answer)