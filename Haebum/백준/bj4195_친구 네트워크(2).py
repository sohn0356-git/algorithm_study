import sys

def find(x):
    global parent
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(x,y):
    global parent
    x = find(x)
    y = find(y)

    if x==y:
        return
    else:
        parent[x] = y
        cnt[y] += cnt[x]

tc = int(sys.stdin.readline())
for _ in range(tc):
    f = int(sys.stdin.readline())
    parent = dict()
    cnt = dict()
    for _ in range(f):
        f1,f2 = sys.stdin.readline().split()
        if not parent.get(f1):
            parent[f1] = f1
            cnt[f1] = 1
        if not parent.get(f2):
            parent[f2] = f2
            cnt[f2] = 1
        union(f1,f2)
        print(cnt[find(f2)])