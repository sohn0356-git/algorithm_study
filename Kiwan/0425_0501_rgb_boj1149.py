# RGB 거리
# 집 RGB색칠하기

N = int(input());
cost = [];
for i in range(N):
    temp = list(map(int, input().split()));
    cost.append(temp);

# print(N);
# print(cost);

res = [[0] * N for _ in range(3)];
# print(res);

def solve(n, p):
    global cost, res;
    if n == 0:
        return 0;
    elif n == 1:
        if res[p][n - 1] == 0:
            res[p][n - 1] = cost[n - 1][p];
        return res[p][n - 1];
    else:
        if res[p][n - 1] == 0:
            if p == 0:
                res[p][n - 1] = min(solve(n - 1, 1), solve(n - 1, 2)) + cost[n - 1][0];
            elif p == 1:
                res[p][n - 1] = min(solve(n - 1, 0), solve(n - 1, 2)) + cost[n - 1][1];
            else:
                res[p][n - 1] = min(solve(n - 1, 0), solve(n - 1, 1)) + cost[n - 1][2];
        return res[p][n - 1];

res = min(solve(N, 0), solve(N, 1), solve(N, 2));
print(res);