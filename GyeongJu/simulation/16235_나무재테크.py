def solutionK(infoTree, arrA, arrAA):
    global N, K 
    trees = 0 

    for i in range(K):
        sands(infoTree, arrAA) 
        fall(infoTree) 
        trees = winter(infoTree, arrAA, arrA) 
    return trees 

def sands(infoTree, arrAA):
    global N 
    # N*N을 돌면서 나무가 있으면 나이 순으로 남은 양분에서 나이값을 뺀다.
    for j in range(N):
        for i in range(N):
            numTrees = len(infoTree[j][i]) 
            if numTrees != 0:
                feed = 1 
                for l in range(numTrees - 1, -1, -1):
                    # feed가 1일 때만 양분을 먹는데,
                    if feed == 1:
                        if arrAA[j][i] >= infoTree[j][i][l]:
                            # 남은 양분이 나무의 나이보다 클 때만 양분을 먹는다.
                            # 나무의 나이도 1 증가한다.
                            arrAA[j][i] -= infoTree[j][i][l] 
                            infoTree[j][i][l] += 1 
                        else:
                            # 남은 양분이 나무의 나이보다 적으면 삭제한다.
                            # 위치는 deadTrees에 저장
                            # 죽은 나무의 위치에 나무의 나이 // 2 를 양분에 더한다.
                            arrAA[j][i] += (infoTree[j][i][l] // 2) 
                            del infoTree[j][i][l] 
                            feed = 0 
                    else:
                        # 한번 feed가 0으로 바뀌면 이후 나무 정보 삭제
                        # 죽은 나무의 위치에 나무의 나이 // 2 를 양분에 더한다.
                        arrAA[j][i] += (infoTree[j][i][l] // 2) 
                        del infoTree[j][i][l] 

def fall(infoTree):
    global N 
    # N*N을 돌면서 나무의 나이가 5의 배수이면 번식한다.
    dx = [-1, -1, -1, 0, 1, 1,  1,  0] 
    dy = [-1,  0,  1, 1, 1, 0, -1, -1] 
    for j in range(N):
        for i in range(N):
            numTrees = len(infoTree[j][i]) 
            if numTrees != 0:
                for l in range(numTrees):
                    if infoTree[j][i][l] % 5 == 0:
                        for n in range(8):
                            nj = dy[n] + j 
                            ni = dx[n] + i 
                            if 0 <= nj < N and 0 <= ni < N:
                                infoTree[nj][ni].append(1) 

def winter(infoTree, arrAA, arrA):
    # 남은 양분에 매년 추가될 양분을 더해준다.
    # N*N 다 도는 김에 나무 개수도 세서 리턴한다.
    global N 
    trees = 0 
    for j in range(N):
        for i in range(N):
            arrAA[j][i] += arrA[j][i] 
            trees += len(infoTree[j][i]) 
    return trees 

N, M, K = map(int, input().split()) 
arrA = [] 
arrAA = [[5] * N for _ in range(N)] 
for i in range(N):
    arrA.append(list(map(int, input().split()))) 

infoTree = [[[] for _ in range(N)] for _ in range(N)] 
startTree = [] 

for j in range(M):
    startTree.append(list(map(int, input().split()))) 

for tree in startTree:
    infoTree[tree[0] - 1][tree[1] - 1].append(tree[2]) 

print(solutionK(infoTree, arrA, arrAA)) 


# 5 2 7
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3
# Answer: 71
#
#
# 10 1 1000
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 1 1 1
# Answer: 5443