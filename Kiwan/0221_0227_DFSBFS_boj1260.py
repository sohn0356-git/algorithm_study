# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]);
    visited[start] = True;
    while queue:
        v = queue.popleft();
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i);
                visited[i] = True;

def dfs(graph, v, visited):
    visited[v] = True;
    print(v, end=' ');
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited);

N, M, V = map(int, input().split());
graph = [];
for i in range(N+1):
    graph.append([]);
visited = [False] * (N + 1);

for i in range(M):
    j, d = map(int, input().split());
    graph[j].append(d);
    graph[d].append(j);

for i in range(N+1):
    graph[i].sort();

dfs(graph, V, visited);
print();
visited = [False] * (N + 1);
bfs(graph, V, visited);
