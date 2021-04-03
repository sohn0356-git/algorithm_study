n,k = map(int,input().split())
line = list(input())

visited = [0]*n
cnt = 0
for i in range(n):
    if line[i] == "P":
        for j in range(-k,k+1):
            if i+j>= 0 and i+j<n:
                if visited[i+j]==0 and line[i+j]=="H":
                    visited[i+j] = 1
                    cnt += 1
                    break

print(cnt)