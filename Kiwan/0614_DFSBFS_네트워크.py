## 네트워크
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [-1] * n
    q = deque()
       
    for i in range(n):
        if visited[i] != 1:
            q.append([i, computers[i]])
            answer += 1

        while q:
            idx, network = q.popleft()
            if visited[idx] != 1:
                visited[idx] = 1
                for j, connect in enumerate(network):
                    if j != idx and connect == 1:
                        q.append([j, computers[j]])
        
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))