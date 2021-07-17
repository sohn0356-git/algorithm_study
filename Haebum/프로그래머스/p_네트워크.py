#bfs로 풀 예정
# 연결되어있는건 1개의 네트워크로 생각함
#토마토랑 비슷한 문제?
from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [[0]*n for _ in range(n)] #방문여부 확인
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == 0: # 연결되어있고 방문했는지 안했는지 확인
                queue.append([i,j]) #큐에 추가
                visited[i][j] = 1 #방문여부에 추가
                answer += 1 #정답 +1

                while(queue): #큐를 돌면서 연결되어있는것들을 다 방문된것으로 처리
                    cur = queue.popleft()
                    for com in range(n):
                        x = cur[0]
                        y = cur[1] + com
                        if y>=0 and y<n:
                            if computers[x][y]== 1 and visited[x][y] == 0:
                                visited[x][y] = 1
                                queue.append([x,y])
                                queue.append([y,0]) #y와 연결되었다는 뜻이므로 y와 연결된것들도 다 큐로 돌것!
            
    print(answer)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


solution(n,computers)