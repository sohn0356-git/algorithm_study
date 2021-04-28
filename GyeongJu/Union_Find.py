def Find(x):
    global parent
    if x == parent[x]:
        return x
    else :
        parent[x] = Find(parent[x])
        return parent[x]

def Union(x,y):
    x = Find(x)
    y = Find(y)

    if x==y:
        return
    parent[x] = y

N = 10
parent = [0]*(N+1)

for i in range(1,N+1):
    parent[i] = i

Union(3,6)
Union(8,6)
Union(8,2)
Union(1,4)
Union(4,10)
Union(7,9)
Union(5,9)

if Find(1) == Find(7):
    print("Team")
else:
    print("Not team")

print(parent[1:])



