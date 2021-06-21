#최대값 최소값 1~50이하

# 브루트포스 가능

# 방문했으면 visited로 표시하고
# 한번 돌때마다 카운트를 올림
# bfs로 풀 예정

#예상 시간복잡도 50^2 정도
#예상 공간복잡도 queue를 이용하므로 미정

from collections import deque

def bfs(w,h):
    #그래프 입력(정사각형)
    graph = [-1]*h
    for m in range(h):
        graph[m] = list(map(int,input().split()))
    #방문여부 확인
    visited = [[0]*(w+1) for _ in range(h+1)]
    queue = deque()
    cnt = 0 # 섬의개수
    #방향백터
    dirR = [-1,1,0,0,1,-1,-1,1]
    dirC = [0,0,-1,1,1,-1,1,-1]

    # 전체 다 돌면서 방문 여부 및 땅인지 확인
    for i in range(h):
        for j in range(w):
            if graph[i][j] ==1 and visited[i][j] == 0:
                queue.append([i,j])
                visited[i][j] = 1
                cnt += 1

                #들어왔으면 갈수 있는곳은 다 가보기(가본곳은 방문한걸로 체크)
                while(queue):
                    cur = queue.popleft()
                    for k in range(8): #방향 백터 돌리기
                        x = cur[0] + dirR[k]
                        y = cur[1] + dirC[k]
                        if x>=0 and x<h and y>=0 and y<w:
                            if graph[x][y] == 1 and visited[x][y] == 0:
                                visited[x][y] = 1
                                queue.append([x,y])
    print(cnt)
    # except:
    #     print(0)
 
#가로 세로 높이 입력
while(True):
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    bfs(w,h)