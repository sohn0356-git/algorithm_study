# n과 m 과 deque를 섞어서 쓰기
# 재귀함수를 통해 문을 3개 다 지었을 경우들을 뽑고
# 벽이 3개 다 지었을때 바이러스를 다 이동시킨 후
# 안전구역 파악하여 정답 비교

#시간복잡도는 벽3개 다 짓는데 8**6 체크하는데 3*8**6 총 8**8 언저리
#공간복잡도 grraph 8*8*4**3 + queue.. 

from collections import deque

n, m = map(int,input().split())
graph = [0]*n
for i in range(n):
    graph[i] = list(map(int,input().split()))

queue = deque()
answer = []
dirR = [0,1,0,-1] #방향백터 설정
dirC = [1,0,-1,0]

#visited = [[0]*m for _ in range(n)]


def doorBuild(stage):
    if stage==3: # 3개의 문을 다 지었을때
        safeZone = 0
        for q in range(n):  #바이러스 시작 위치 집어넣기
            for w in range(m):
                if graph[q][w] == 2:
                    queue.append([q,w])

        while(queue): #바이러스 전파
            cur = queue.popleft()
            for vec in range(4):
                x = cur[0] + dirR[vec]
                y = cur[1] + dirC[vec]
                if x>=0 and x<n and y>=0 and y<m:
                    if graph[x][y] == 0:
                        graph[x][y] = 3 #바이러스 전파한곳
                        queue.append([x,y])

        for c in range(n): #안전구역 체크
            for v in range(m):
                if graph[c][v] == 0:
                    safeZone +=1
        answer.append(safeZone) #현재 안전구역 갯수를 정답리스트에 집어넣기

        for ai in range(n): #바이러스 전파 초기화
            for aj in range(m):
                if graph[ai][aj] == 3:
                    graph[ai][aj] = 0
        return #종단

    for a in range(n): #문생성
        for b in range(m):
            if graph[a][b] == 0:
                graph[a][b] = 1 #문을 짓고
                doorBuild(stage+1) #문 더 지으러 가자
                graph[a][b] = 0 #문을 안지었을때로 돌려줌
                

doorBuild(0)
print(max(answer))