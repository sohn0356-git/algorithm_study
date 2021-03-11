n, m = map(int, input().split());

used = [0] * m;
visited = [0] * n;
card = [];

for i in range(1, n+1):
    card.append(i);

def solve(stage) :
    if stage == m :
        for i in used :
            print(card[i], end = ' ');
        print();
        return;

    for i in range(0,n) :
        if stage > 0 and i <= used[stage-1]:
            continue;
        if visited[i] == 0 :
            visited[i] = 1;
            used[stage] = i;
            solve(stage + 1);
            visited[i] = 0;

solve(0);

