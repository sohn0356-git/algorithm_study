N = int(input())
T = []
P = []

for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

def solve(stage):
    if stage == N:
        return 0
    if stage > N:
        return -987654321
    return max(P[stage] + solve(stage+T[stage]),solve(stage+1))

print(solve(0))