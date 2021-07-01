def Find(x):
    global parent
    if x == parent[x]:
        return x
    else:
        y= Find(parent[x])
        parent[x] = y
        return y

    # else :
    #     parent[x] = Find(parent[x])
    #     return parent[x]

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

Union(4,3)
print(parent)
Union(3,2)
print(parent)
Union(2,1)
print(parent)
# Union(1,4)
# Union(4,10)
# Union(7,9)
# Union(5,9)
Find(3)
print(parent)
# if Find(4) == Find(5):
#     print("Team")
# else:
#     print("Not team")

# print(parent[1:])