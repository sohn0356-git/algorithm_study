N = int(input())
MOD = 10007
# DP = [-1] * 1001

# def solve(stage):
#     global DP
#     if stage==0 or stage==1:
#         return 1

#     if DP[stage] == -1:
#         DP[stage] = solve(stage-1)+solve(stage-2)
#     return DP[stage]

DP = [0]*1003
DP[0] = 1
DP[1] = 2

for i in range(N+1):
    DP[i+2] = DP[i+1] + DP[i]

print(DP[N])