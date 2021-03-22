# https://www.acmicpc.net/problem/11726
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 출력: 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
import sys

sys.setrecursionlimit(10 ** 6)
mod = 10007


# nC0 + n-1C1 + n-2C2 + n-3C3 + ...
def recur(j, k):
    if k > j - k:  # nCk = nCn-k
        k = j - k
    if solved[k][j]:
        return solved[k][j]
    else:
        if j == 0:
            return 0
        elif j == 1:
            solved[k][j] = 1
            return 1
        else:  # n >= 2
            if k == 2:
                result = (j * (j - 1) // 2) % mod
            elif k == 1:
                result = j
            elif k == 0:
                result = 1
            else:
                result = ((recur(j - 1, k - 1) % mod) + (recur(j - 1, k) % mod)) % mod
            solved[k][j] = result
            return result


if __name__ == "__main__":
    n = int(input())
    solved = [[0 for _ in range(n + 1)] for _ in range(n // 2 + 1)]
    SUM = 0
    for i in range(n // 2 + 1):
        SUM = (SUM + recur(n - i, i)) % mod
    print(SUM)
