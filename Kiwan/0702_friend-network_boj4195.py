def Find(x, parent):
    if x == parent[x]:
        return x
    else :
        parent[x] = Find(parent[x], parent)
        return parent[x]

# y부모 - x자식 관계 만들어주는 함수
def Union(x, y, parent):
    # 루트를 찾는다.
    x = Find(x, parent)
    y = Find(y, parent)
    # 루트가 같다면 같은 트리이므로 합칠 필요가 없음
    if x==y:
        return
    # x의 루트를 y로 바꿈
    parent[x] = y
    # 자식노드를 루트로 하는 집합의 원소 개수를 부모노드를 루트로 하는 집합 원소 개수에 합해준다.
    setCount[y] += setCount[x]
    # 자식노드를 루트로 하는 집합의 원소 개수는 1이 된다. 자식노드 1개.
    setCount[x] = 1

answer = []
TC = int(input())
for _ in range(TC):
    F = int(input())
    parent = dict() # 부모 정보를 담을 딕셔너리
    setCount = dict() # 루트노드 집합에 포함된 원소 개수를 담을 딕셔너리, 리프노드의 값은 1로 바꿔준다.
    for i in range(F):
        f1, f2 = input().split()
        if parent.get(f1) == None:
            parent[f1] = f1
            setCount[f1] = 1
        if parent.get(f2) == None:
            parent[f2] = f2
            setCount[f2] = 1
        Union(f1, f2, parent) # f1의 부모는 f2가 된다.
        answer.append(setCount[Find(f2, parent)])

for elem in answer:
    print(elem)
# 2
# 3
# Fred Barney
# Barney Betty
# Betty Wilma
# 3
# Fred Barney
# Betty Wilma
# Barney Betty