# 다리 놓기

# Top down
def bridge(N, M):
    # MCN = M-1CN-1 + M-1CN
    global mcn;
    if N == 0:
        if mcn[M][N] == -1:
            mcn[M][N] = 1;
        return mcn[M][N];
    elif N == 1:
        if mcn[M][N] == -1:
            mcn[M][N] = M;
        return mcn[M][N];
    elif M == N:
        if mcn[M][N] == -1:
            mcn[M][N] = 1;
        return mcn[M][N];
    else:
        if mcn[M][N] == -1:
            mcn[M][N] = bridge(N - 1, M - 1) + bridge(N, M - 1);
        return mcn[M][N];

T = int(input());
for _ in range(T):
    N, M = map(int, input().split());
    mcn = [[-1] * (M + 1) for _ in range(M + 1)];
    print(bridge(N, M));

# 53
# 42         43
# 31    32
# 20 21 21 22