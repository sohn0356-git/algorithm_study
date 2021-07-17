# 유니온 파인드 외우기

def Find(x, parent):
    if x == parent[x]:
        return x
    else:
        parent[x] = Find(parent[x], parent)
        return parent[x]

def Union(x, y, parent):
    x = Find(x, parent)
    y = Find(y, parent)

    if x == y:
        return

    parent[x] = y

parent = [i for i in range(10)]

print(parent)
Union(2,3,parent)
Union(3,4,parent)
Union(4,5,parent)
Union(5,6,parent)
print(parent)
Find(2,parent)
print(parent)