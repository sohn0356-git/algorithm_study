def solve(n, k):
    global DP, MOD
    if n==k or k==0:
        return 1
    if k==1 or k==n-1:
        return n
    if DP[n][k]==-1:
        DP[n][k] = solve(n-1,k)%MOD + solve(n-1,k-1)%MOD
        DP[n][k] %= MOD
    return DP[n][k]  

N, K = map(int, input().split())
DP = [[-1]*1001 for _ in range(1001)]
MOD = 10007
print(solve(N,K))
