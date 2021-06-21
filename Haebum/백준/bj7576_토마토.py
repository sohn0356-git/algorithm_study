#bfs로 풀어야함
from collections import deque

#상자크기 (행m,열n)
m,n = map(int,input().split())

#상자생성
graph = [0]*n

for i in range(n):
    graph[i] = list(map(int,input().split()))

#방문했는지 안했는지 체크
visited = [[-1]*m for _ in range(n)] 

#객체 생성
queue = deque()

#시작지점 체크
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])
            visited[i][j] = 0

#좌표변동을 위한 리스트(상우하좌)
dirR = [0,1,0,-1]
dirC = [1,0,-1,0]

answer = 0

#큐가 있는동안
while queue:
    cur = queue.popleft() #큐의 좌측에서 하나씩 꺼내기
    for i in range(4): #4방향 한번씩 가보기
        x = cur[0] + dirR[i] 
        y = cur[1] + dirC[i]
        #간곳의 좌표가 마이너스가 아니면서 최대치를 안넘는다
        if (0<=x and x<n) and (0<=y and y<m):
            if graph[x][y] == 0 and visited[x][y]==-1 : #안익은 토마토가 있고, 방문하지 않은 곳이다!
                visited[x][y] = visited[cur[0]][cur[1]] +1 #방문한곳의 깊이는 이전깊이의 +1
                graph[x][y] = 1 #익은토마토로 변경
                queue.append([x,y]) #큐에 현재좌표 담기
                answer = visited[x][y] #정답을 현재깊이로 변경

#다 한 후에도 안익은 토마토가 있다면?
for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer = -1
print(answer)

#시간복잡도 10**6
