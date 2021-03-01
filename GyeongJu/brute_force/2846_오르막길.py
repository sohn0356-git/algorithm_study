N = int(input())
P = list(map(int, input().split(' ')))

ans = 0
start = 0
end = 0

for i in range(1,len(P)):
    if P[i-1] < P[i]:
        end += 1
    else :
        h = P[end]-P[start]
        if ans < h:
            ans = h
        start = i
        end = i
h = P[end]-P[start]
if ans < h:
    ans = h
print(ans)

