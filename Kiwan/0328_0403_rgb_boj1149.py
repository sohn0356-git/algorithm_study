# RGB거리

# Bottom up - 실패
# def dp(N):
#     global rgb, res;
#     res[0][1] = rgb[0][0];
#     res[1][1] = rgb[0][1];
#     res[2][1] = rgb[0][2];
#     for n in range(2, N + 1):
#         for i in range(3):
#             if res[i][n] == -1:
#                 idx = rgb[n - 2].index(res[i][n - 1]);
#                 if idx == 0:
#                     res[i][n] = min(rgb[n - 1][idx + 1 : ]);
#                 elif idx == 2:
#                     res[i][n] = min(rgb[n - 1][ : idx]);
#                 else:
#                     res[i][n] = min(rgb[n - 1][ : idx] + rgb[n - 1][idx + 1 : ]);

def dp(N, num):
    global rgb, res;
    if N == 1:
        if ifcal[1] == -1:
            res[0][1] = rgb[0][0];
            res[1][1] = rgb[0][1];
            res[2][1] = rgb[0][2];
            ifcal[N] = 1;
        if num == 0:
            return res[0][1];
        elif num == 1:
            return res[1][1];
        else:
            return res[2][1];
    else:
        if ifcal[N] == -1:
            res[0][N] = min(dp(N - 1, 1) + rgb[N - 1][0], dp(N - 1, 2) + rgb[N - 1][0]);
            res[1][N] = min(dp(N - 1, 0) + rgb[N - 1][1], dp(N - 1, 2) + rgb[N - 1][1]);
            res[2][N] = min(dp(N - 1, 0) + rgb[N - 1][2], dp(N - 1, 1) + rgb[N - 1][2]);
            ifcal[N] = 1;
        if num == 0:
            return res[0][N];
        elif num == 1:
            return res[1][N];
        else:
            return res[2][N];


N = int(input());
rgb = [];
res = [[-1] * (N + 1) for _ in range(3)];
ifcal = [-1] * (N + 1);
for i in range(N):
    temp = list(map(int, input().split()));
    rgb.append(temp);
dp(N, 1);
# print(res);
print(min(res[0][-1], res[1][-1], res[2][-1]));

# 2
# 20 30 40
# 40 50 20

# 3
# 1 9 2
# 1 9 9
# 9 1 9

# 3
# 1 20 30
# 50 5 6
# 9 3 7

# 3
# 10 40 60
# 20 13 14
# 20 14 19

# 5
# 5 5 5
# 4 1 1
# 5 3 5
# 4 5 2
# 1 3 5

# 5
# 5 4 4
# 2 2 3
# 3 2 2
# 2 1 2
# 1 3 1