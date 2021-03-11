import sys
sys.setrecursionlimit(10**6)

def solve(n):
    global DP
    if n==1:
        return 0
    if DP[n]==0:
        DP[n] = 1+solve(n-1)
        if n%3==0:
            t3 = 1 + solve(n//3)
            DP[n] = min(DP[n],t3)
        if n%2==0:
            t2 = 1 + solve(n//2)
            DP[n] = min(DP[n],t2)
        
    return DP[n]


N = int(input())
DP = [0]*1000001
print(solve(N))