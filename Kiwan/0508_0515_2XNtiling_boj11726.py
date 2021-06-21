def solve(N):
    global res;
    if N == 0:
        res[n] = 1;
        return res[N] % 10007;
    elif N == 1:
        if res[N] != -1:
            return res[N] % 10007;
        else:
            res[N] = 1;
            return res[N] % 10007;
    elif N == 2:
        if res[N] != -1:
            return res[N] % 10007;
        else:
            res[N] = 2;
            return res[N] % 10007;
    else:
        if res[N] != -1:
            res[N] %= 10007;
            return res[N] % 10007;
        else:
            for i in range(3, N + 1):
                res[N] = (solve(N - 1) % 10007 + solve(N - 2) % 10007) % 10007;
            return res[N] % 10007;

n = int(input());
res = [-1] * 1001;
print(solve(n));