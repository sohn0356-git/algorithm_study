import sys
from collections import deque

#작년순위에 따른 진입차수 설정 및 그래프 연결
# 5-> 4 -> 3- > 2-> 1

# 5 <- 4 3 2 1 진입차수: 4
# 4 <- 3 2 1 진입차수: 3
# 3 <- 2 1 진입차수:2
# 2 <- 1 진입차수:1

# 순위 변동에 따른 그래프 변동 및 진입차수 변동

# 그후 위상정렬

# 해당 조건에 따른 리턴값 반환

def topological():
    queue = deque()

    #진입차수 0 -> queue 삽입
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)

    #위상정렬
    result = []

    for _ in range(n):
        if len(queue) == 0: #큐에 아무것도 없게되면 정상적인 결과 x
            return "IMPOSSIBLE"
        cur = queue.popleft()
        result.append(cur)
        for q in range(len(graph[cur])):
            indegree[q] -= 1
            if indegree[q] == 0:
                queue.append(q)
                if len(queue)>=2: #결과가 2개 이상이 가능한 경우
                    return "?"
    return result


tc = int(sys.stdin.readline()) #테스트케이스 수

for i in range(tc): 
    n = int(sys.stdin.readline()) # 팀 숫자
    graph = [[False]*(n+1) for _ in range(n+1)] #그래프
    indegree = [0]*(n+1) # 진입차수
    last_year = list(map(int,sys.stdin.readline().split())) #작년순위
    m = int(sys.stdin.readline()) #순위 변동 수

    # 자신보다 순위 숫자가 낮은값으로 연결
    # ex) graph[5][4] = true , graph[5][3] = true ... graph[4][3] = true 5가 4보다 순위 숫자가 높으면 트루
    # indgree도 증가
    for x in range(n):
        for y in range(x+1,n):
            graph[last_year[x]][last_year[y]] = True
            indegree[last_year[y]] += 1

    #순위 변동
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split()) #a,b가 순위 변경되었을때
        if not graph[a][b]: # a<b일때 -> a>b로 변경해야함
            graph[b][a] = False # a<b는 false로 변경(그래프 원상태로)
            indegree[a] -= 1 #진입차수 다시 감소
            graph[a][b] = True # a>b로 변경 (그래프 이어진걸로)
            indegree[b] += 1 #진입차수 증가
        else: # a>b일때 -> b>a로 변경
            graph[b][a] = True
            indegree[a] += 1
            graph[a][b] = False
            indegree[b] -= 1

    
    answer = topological() #위상정렬 결과 담기

    if answer == "IMPOSSIBLE":
        print(answer)
    elif answer == "?":
        print(answer)
    else:
        for _ in answer:
            print(_,end=" ")
        print()