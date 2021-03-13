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
    ck = 0
    if stage==M:
        for i in used:
            print(card[i], end=' ')
        print()
        #print(used)
        return

    for i in range(N):
        if stage > 0 and i < used[stage - 1]:
            continue
        if ck != card[i]:
            used[stage] = i
            ck = card[i]
            solve(stage + 1)


solve(0)
