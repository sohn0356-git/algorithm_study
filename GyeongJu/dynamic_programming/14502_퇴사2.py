N = int(input())
T = []
P = []
DP = [0]*(N+1)
for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

for i in range(N):
    if i+T[i]<=N:
        DP[i+T[i]] = max(DP[i+T[i]],DP[i]+P[i])
    DP[i+1] = max(DP[i+1],DP[i])

print(DP[N])