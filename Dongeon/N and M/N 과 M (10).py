
n, m = map(int, input().split());

card = list(map(int, input().split()));
card.sort();

used = [0] * m;
visited = [0] * n;


def solve(stage) :
    checker = 0;

    if stage == m :
        for i in used :
            print(card[i], end = " ");
        print();
        return

    for i in range(n) :
        if stage > 0 and i < used[stage - 1]:
            continue;
        if visited[i] == 0 and checker != card[i]:
                visited[i] = 1;
                used[stage] = i;
                checker = card[i];
                solve(stage + 1);
                visited[i] = 0;

solve(0);
