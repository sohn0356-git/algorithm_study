
## top down
# def tile(n):
#     global res;
#     if n == 1:
#         res[0] = 1;
#         return res[0];
#     elif n == 2:
#         res[1] = 2;
#         return res[1];
#     elif n >= 3:
#         res[n - 1] = (res[n - 2] % 10007 + res[n - 3] % 10007) % 10007;
#         return (tile(n - 1) + tile(n - 2)) % 10007;

## bottom up
def tile(n):
    res[0] = 1; res[1] = 2;
    if n <= 2:
        return res[n - 1];
    else:
        for i in range(2, n):
            res[i] = (res[i - 1] % 10007 + res[i - 2] % 10007) % 10007;
        return res[n - 1] % 10007;

n = int(input());
res = [0] * 10007;
print(tile(n));
