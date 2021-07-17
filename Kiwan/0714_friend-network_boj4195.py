def Find(x, parent):
    if parent[x] == x:
        return x
    else:
        parent[x] = Find(parent[x], parent)
        return parent[x]

# x의 부모를 y로 만들어준다
def Union(x, y, parent, countNodes):
    # 루트를 찾는다
    x = Find(x, parent)
    y = Find(y, parent)
    # 루트가 같으면 같은 트리이므로 합치지 않음
    if x == y:
        return
    # x의 루트를 y로 바꾼다
    parent[x] = y
    countNodes[y] += countNodes[x]
    countNodes[x] = 1


answer = []
TC = int(input())
for i in range(TC):
    networks = []
    parent = dict()
    countNodes = dict()
    F = int(input())
    for j in range(F):
        networks.append(input().split())
    for network in networks:
        x, y = network
        # x, y가 parent 딕셔너리에 없으면 새로 만들어준다
        if parent.get(x) == None:
            parent[x] = x
        if parent.get(y) == None:
            parent[y] = y
        # x, y 각각 자기자신 포함 하위 노드의 개수를 세는 딕셔너리 원소로 만들어준다
        if countNodes.get(x) == None:
            countNodes[x] = 1
        if countNodes.get(y) == None:
            countNodes[y] = 1
        # x의 부모를 y로 바꿔준다
        Union(x,y,parent,countNodes)
        # print(parent)
        # print(countNodes)
        answer.append(countNodes[Find(y, parent)])

for ans in answer:
    print(ans)