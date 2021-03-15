n, m = map(int,input().split())

used = [0] * m
visited = [0] * (n + 1)

card = list(map(int, input().split()))
card.sort()

for i in range(1, n + 1):
    card.append(i)

def solve(stage):
    num = 0
    if stage == m:
        for i in used:
            print(card[i], end=" ")
        print()
        return
    for i in range(n):
        if stage > 0 and i < used[stage - 1]:
            continue
        if visited[i] == 0 and num != card[i]:
            visited[i] = 1
            num = card[i]
            used[stage] = i
            solve(stage + 1)
            visited[i] = 0

solve(0)
