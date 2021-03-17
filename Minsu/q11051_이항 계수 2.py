# https://www.acmicpc.net/problem/11051
# 자연수 과 정수 가 주어졌을 때 이항 계수 nCk를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)
# 출력: nCk를 10,007로 나눈 나머지를 출력한다.
import sys
sys.setrecursionlimit(10 ** 6)
mod = 10007


def recur(n, k):
    if k > n - k:  # nCk = nCn-k
        k = n - k
    if solved[k][n]:
        return solved[k][n]
    else:
        if n == 0:
            return 0
        elif n == 1:
            solved[k][n] = 1
            return 1
        else:  # n >= 2
            if k == 2:
                result = (n * (n - 1) // 2) % mod
            elif k == 1:
                result = n
            elif k == 0:
                result = 1
            else:
                result = ((recur(n - 1, k - 1) % mod) + (recur(n - 1, k) % mod)) % mod
            solved[k][n] = result
            return result


if __name__ == "__main__":
    N, K = map(int, input().split())
    solved = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
    print(recur(N, K))