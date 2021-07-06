import sys

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x,y):
    global par
    x = find(x)
    y = find(y)
    if x==y:
        return
    par[y] = x
    num[x] += num[y]

tc = int(sys.stdin.readline())

for _ in range(tc):
    fnum = int(sys.stdin.readline())
    par = dict()
    num = dict()
    for _ in range(fnum): #10^6
        one, two = sys.stdin.readline().replace("\n","").split(" ")

        if not par.get(one):
            par[one] = one
            num[one] = 1
        if not par.get(two):
            par[two] = two
            num[two] = 1
        union(one,two)
        print(num[find(one)])