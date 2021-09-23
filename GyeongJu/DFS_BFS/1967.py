import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(dir, node):
    global graph, n, answer

    if len(graph[node]) == 0:
        return 0

    data = []
    for i in range(len(graph[node])):
        data.append(graph[node][i][1] + solve(i, graph[node][i][0]))
    f, s = -1, -1
    for i in data:
        if f == -1:
            f = i
        elif s == -1:
            if f < i:
                f, s = i, f
            else:
                s = i
        else:
            if f < i:
                f, s = i, f
            elif s < i:
                s = i

    answer.append(max(f, 0) + max(s, 0))
    return f

n = int(input())
graph = [[] for _ in range(10001)]
graph[0].append([1,0])
for i in range(n-1):
    edge = list(map(int, input().split()))
    graph[edge[0]].append([edge[1], edge[2]])

answer = [0]*10001
solve(0,0)
print(max(answer))