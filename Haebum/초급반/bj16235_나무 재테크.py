

# 해보면서 파악 예정
# 봄,여름,가을,겨울 별로 별도 구현
# 설정은 잘 했으나, 다중차원시의 디테일 부족으로 인한 오류 다수...
# 추후 양분과 산나무,죽은나무 표시를 별도로 뺌


import sys

# n 밭의 크기 m 나무의 개수 k 최종년수
n,m, k = map(int,sys.stdin.readline().split()) 
# 밭 설정
graph = [[[0]*2 for _ in range(n)] for _ in range(n)]
#양분 설정
A = [list(map(int,sys.stdin.readline().split())) for _ in range(n) ]
# 초기 밭 양분 설정
for width in range(n):
    for height in range(n):
        graph[width][height] = [A[width][height],0]
# 초기 나무 나이 설정
for j in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    if graph[x-1][y-1][1] == 0:
        graph[x-1][y-1][1] = [[1,z]]
    else:
        graph[x-1][y-1][1].append([1,z])


#가을 돌릴 큐 생성
queue = deque()

#방향백터설정
dirC = [0,1,0,-1,-1,1,1,-1]
dirR = [1,0,-1,0,-1,1,-1,1]

#년차수만큼 돌기
for a in range(k):
    # 봄
    for width in range(n):
        for height in range(n):
            trees = graph[width][height][1] #그칸의 나무들
            food = graph[width][height][0] #양분
            if trees:
                trees = sorted(trees, key = lambda x : x[1]) #나무의 나이 기준으로 정렬
                for tree in trees: # 양분이 나무의 나이보다 많을때
                    if tree[0] == 1:
                        if food >= tree[1]:
                            food -= tree[1]
                            tree[1] += 1
                        else:
                            tree[0] = 2 #나무를 죽은나무로 표기
                    elif tree[0] == 0:
                        trees.remove(tree)
            else:
                pass
    #여름
    for width in range(n):
        for height in range(n):
            #맵에 죽은나무가 있을때
            trees = graph[width][height][1] #그칸의 나무들
            food = graph[width][height][0] #양분
            if trees:
                for tree in trees:
                    if tree[0] == 2: #죽은 나무일때
                        food += (tree[1]/2)
                        tree = [0,0] #없는걸로 변환
            else:
                pass
    
    #가을
    for width in range(n):
        for height in range(n):
            trees = graph[width][height][1] #그칸의 나무들
            if trees:
                for tree in trees:
                    if tree[0] == 1: #살아있는 나무가 있을때
                        if tree[1]%5 ==0: 
                            queue.append([width,height])
            else:
                pass
    
    #가을 전파
    while queue:
        cur = queue.popleft()
        for vec in range(8):
            xx = cur[0] + dirR[vec]
            yy = cur[1] + dirC[vec]
            if x>=0 and x<n and y>=0 and y<m:
                graph[xx][yy][1].append([1,1])
    
    #겨울
    for width in range(n):
        for height in range(n):
            graph[width][height][0] += A[width][height]

answer = 0
for width in range(n):
    for height in range(n):
        trees = graph[width][height][1]
        if trees:
            for tree in trees:
                if tree[0] == 1:
                    answer += 1
        else:
            pass

print(answer)