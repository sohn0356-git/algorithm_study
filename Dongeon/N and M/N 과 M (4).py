"""
    같은 수를 여러번 골라도 된다.
    고른 수열은 비내림차순


"""

n,m = map(int, input().split())

used = [0] * m
visited = [0] * n

card = []
for i in range(1,n+1):
    card.append(i)

def solve(stage) :
    if stage == m :
        for i in used :
            print(card[i], end = " ");
        print();
        return

    for i in range(n) :
        if stage > 0 and i < used[stage - 1]:
            continue;
        used[stage] = i;
        solve(stage + 1);

solve(0);