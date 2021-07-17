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
    # 루트가 같으면 그냥 리턴
    if x == y:
        return
    parent[x] = y
    answer += weight

V, E = list(map(int, sys.stdin.readline().rstrip().split()))
weightList = []
parent = dict()
answer = 0
for i in range(E):
    weightList.append(list(map(int, sys.stdin.readline().rstrip().split())))

weightList.sort(key = lambda x:(x[2], x[0]))

for elem in weightList:
    x, y, weight = elem
    if parent.get(x) == None:
        parent[x] = x
    if parent.get(y) == None:
        parent[y] = y

    Union(y, x, parent, weight)

print(answer)