from collections import deque

T = int(input())
for tc in range(T):
    cnt = 1
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dirR = [1,0,-1,0]
    dirC = [0,1,0,-1]

    for i in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1



    for i in range(N):
        for j in range(M):
            if visited[i][j]==0 and arr[i][j]==1:
                queue = deque()
                queue.append((i,j))
                visited[i][j]=cnt
                while queue:
                    cur = queue.popleft()
                    for d in range(4):
                        nR = cur[0] + dirR[d]
                        nC = cur[1] + dirC[d]
                        if nR>=0 and nR<N and nC>=0 and nC<M:
                            if visited[nR][nC]==0 and arr[nR][nC]==1:
                                visited[nR][nC]=cnt
                                queue.append((nR,nC))
                cnt+=1

    print(cnt-1)