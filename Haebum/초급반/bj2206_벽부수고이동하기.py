# bfs로 풀 예정
# 근데 벽을 깻냐 안깻냐는게 필요
# visited와 벽을 깻냐 안깻냐는 체크가 하나 더 필요할것으로 보임?
# 방향 x,y를 저장할때 벽을깻냐 안깻냐도 저장해버리기

#그럼 시간복잡도는 1000*1000 = 10^3*10^3 = 10^6이므로 이중포문형태까진 가능
# 공간복잡도도 비슷할 것으로 예상

from collections import deque


def bfs():
    queue = deque()
    queue.append([0,0,0]) #좌표 x,y와 벽뿌신여부
    visited[0][0][0] = 1 #첫좌표 1

    if n ==1 and m==1: #1행1열일때 리턴값 
        return 1

    while(queue):
        cur = queue.popleft()
        if cur[0] == n-1 and cur[1] == m-1: #마지막 도착했을때
            return visited[cur[0]][cur[1]][cur[2]] #이동횟수 리턴
        for i in range(4): #4방향 다 가보기
            x = cur[0] + dirC[i]
            y = cur[1] + dirR[i]
            z = cur[2]
            if x>=0 and x<n and y>=0 and y<m: #이동가능한 곳일때
                if visited[x][y][z] ==0 and graph[x][y] == 0: #방문안했고 벽이 아니다!
                    visited[x][y][z] = visited[cur[0]][cur[1]][cur[2]] +1 #방문한곳의 이동횟수 이전이동횟수의 +1
                    queue.append([x,y,z]) #좌표와 기존에 벽부순 유무 저장
                elif z == 0 and visited[x][y][z] == 0 and graph[x][y] == 1: #벽을 아직 안부쉈는데 방문안했고 벽이 있다!
                    visited[x][y][1] = visited[cur[0]][cur[1]][cur[2]] +1 #벽을 부쉈고 그 좌표에 이동횟수 +1
                    queue.append([x,y,1]) #좌표와 벽을 부순걸로 표시
    
    return -1 #불가능할시 리턴값


n, m = map(int,input().split())
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] #방문여부 및 방문시의 이동횟수 저장
graph = [list(map(int,input().strip())) for _ in range(n)] #맵

#방향백터(우,하,좌,상)
dirC = [0,1,0,-1] 
dirR = [1,0,-1,0]

print(bfs())
