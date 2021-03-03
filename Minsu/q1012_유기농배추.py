# https://www.acmicpc.net/problem/1012
# 입력: 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
# 출력: 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

def dfs(M, N):
    stack = []
    cnt = 0
    while notVisited or stack:
        if stack:
            X, Y = stack.pop()
            for i, j in ((X - 1, Y), (X + 1, Y), (X, Y - 1), (X, Y + 1)):
                # (i, j)에 배추가 있는지 확인한다. 없으면 ValueError가 뜨므로 try, except 사용
                # 있으면 notVisited에서 삭제하고 stack에 넣는다.
                    try:
                        stack.append(notVisited.pop(notVisited.index((i, j))))
                    except:
                        pass
        else:  # 스택이 비었을 때(현재 더 이상 연결된 배추가 없을 때)
            stack.append(notVisited.pop())
            cnt += 1  # 지렁이 추가
    return cnt


def run_case():
    M, N, K = map(int, input().split())
    for _ in range(K):
        X, Y = map(int, input().split())
        notVisited.append((X, Y))
    print(dfs(M, N))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        notVisited = []
        run_case()
