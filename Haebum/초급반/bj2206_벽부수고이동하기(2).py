# bfs로 풀 예정
# 근데 벽을 깻냐 안깻냐는게 필요
# visited와 벽을 깻냐 안깻냐는 체크가 하나 더 필요할것으로 보임?
# 방향 x,y를 저장할때 벽을깻냐 안깻냐도 저장해버리기

#그럼 시간복잡도는 1000*1000 = 10^3*10^3 = 10^6이므로 이중포문형태까진 가능
# 공간복잡도도 비슷할 것으로 예상

from collections import deque


def bfs(a,b,d):
    queue = deque()
    queue.append([a,b,d]) #좌표 x,y와 벽뿌신여부
    visited[0][0] = 1

    while(queue):
        cur = queue.popleft()
        if cur[0] == n-1 and cur[1] == m-1:
            answer.append(visited[cur[0]][cur[1]])
            continue
        for i in range(4):
            x = cur[0] + dirC[i]
            y = cur[1] + dirR[i]
            c = cur[2]
            if x>=0 and x<=(n-1) and y>=0 and y<=(m-1):
                if c==1: #벽을 이미 한번 부셨을 경우
                    if visited[x][y] ==-1 and graph[x][y] == 0:
                        visited[x][y] = visited[cur[0]][cur[1]] +1 #방문한곳의 깊이는 이전깊이의 +1
                        queue.append([x,y,1])
                else: #벽을 아직 안부셨을 경우
                    if visited[x][y] == -1 and graph[x][y] == 0: #이동한 곳이 벽이 아닌경우
                        visited[x][y] = visited[cur[0]][cur[1]] +1
                        queue.append([x,y,0])
                    elif visited[x][y] == -1 and graph[x][y] == 1: #이동한 곳이 벽일 경우
                        visited[x][y] = visited[cur[0]][cur[1]] +1 
                        bfs(x,y,1)
n, m = map(int,input().split())
visited = [[-1]*(m) for _ in range(n)] #방문여부 및 방문시의 이동횟수 저장
graph = [list(map(int,input().strip())) for _ in range(n)] #맵

#방향백터
dirC = [0,1,0,-1]
dirR = [1,0,-1,0]

#정답
answer = [] #초기값 -1

bfs(0,0,0)
if answer:
    print(min(answer))
else:
    print(-1)