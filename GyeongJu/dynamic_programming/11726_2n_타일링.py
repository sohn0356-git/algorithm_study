def solve(n):
    global DP, MOD
    if n==0 or n==1:
        return 1
    if DP[n]==-1:
        DP[n] = solve(n-1)%MOD + solve(n-2)%MOD
        DP[n] %= MOD
    return DP[n]

N = int(input())
MOD = 10007
DP = [-1]*1001

print(solve(N))