# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

N, M = map(int, input().split())

used = [0]*M
visited = [0]*N
card = list(map(int, input().split()))
card.sort()

for i in range(1,N+1):
    card.append(i)

def solve(stage): #재귀함수
    if stage==M:
        for i in used:
            print(card[i], end=' ')
        print()
        #print(used)
        return

    for i in range(N):
        if stage > 0 and i < used[stage - 1]:
            continue
        used[stage] = i
        solve(stage + 1)  ##여기서 재귀

solve(0)
