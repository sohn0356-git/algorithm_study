
#   오른 왼 위 아래 1시 11시 7시 5시
from collections import deque

dx = [1,-1,0, 0,1,-1,-1, 1]
dy = [0, 0,1,-1,1, 1,-1,-1]

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break;

    islands = [0]*h
    for i in range(h):
        islands[i] =list(map(int,input().split()))
    #print(islands)

    dQ = deque()
    cnt = 0
    visited = [[0]*w for _ in range (h)] #deep copy
    #visited2 = [[0]*w]*h #shallow copy

    for i in range(h):
        for j in range(w):
            if islands[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                #islands[i][j] = 2
                dQ.append((i,j)) #세로 가로
                while dQ:
                    #현재위치 팝
                    tempX, tempY = dQ.popleft()
                    for k in range(8):
                        nextX = tempX +dx[k] #세로, Y축
                        nextY = tempY +dy[k]
                        if 0 <= nextX and nextX < h and 0 <= nextY and nextY <w:  # 왜 h랑 w?  w랑 h 아니고?
                            if islands[nextX][nextY]==1 and visited[nextX][nextY]==0: #and 뒤에 빼기
                                visited[nextX][nextY]=1
                                #islands[nextX][nextY] = 2
                                dQ.append((nextX,nextY))

                cnt +=1

    print(cnt)

