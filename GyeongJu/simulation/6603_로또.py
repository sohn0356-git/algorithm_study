
def solve(stage):
    global K, used, visited, card
    if stage==6:
        for i in used:
            print(card[i], end=' ')
        print()
        return

    for i in range(K):
        if visited[i]==0:
            if stage>0 and used[stage-1]>=i:
                continue
            visited[i] = 1
            used[stage] = i
            solve(stage+1)
            visited[i] = 0

while True:
    card = list(map(int, input().split()))
    K = card[0]
    if K==0:
        break
    card = card[1:]

    used = [0] * 6
    visited = [0] * K
    solve(0)
    print()
