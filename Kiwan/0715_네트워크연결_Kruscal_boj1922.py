import sys

def Find(x, parent):
    if x == parent[x]:
        return x
    else:
        parent[x] = Find(parent[x], parent)
        return parent[x]

def Union(x, y, parent, weight):
    global answer
    x = Find(x, parent)
    y = Find(y, parent)

    if x == y:
        return

    parent[x] = y
    answer += weight

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
answer = 0
parent = dict()
infoes = []
for i in range(M):
    infoes.append(list(map(int,sys.stdin.readline().rstrip().split())))

infoes.sort(key = lambda x : (x[2], x[0]))

for info in infoes:
    u, v, weight = info
    if parent.get(u) == None:
        parent[u] = u
    if parent.get(v) == None:
        parent[v] = v

    Union(v, u, parent, weight)

# print(parent)
print(answer)

