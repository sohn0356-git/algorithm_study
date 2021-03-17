




boolean = 1
while boolean :
    list1 = list(map(int, input().split()))

    if list1[0] == 0 :
        boolean = 0;

    n = list1[0];
    m = 6;
    used = [0] * m;
    visited = [0] * n;
    card = [];

    for i in range(1, len(list1)) :
        card.append(list1[i])


    def solve(stage):
        if stage == m:
            for i in used:
                print(card[i], end=' ');
            print();
            return

        for i in range(n):
            if stage > 0 and i <= used[stage - 1]:
                continue
            if visited[i] == 0:
                visited[i] = 1;
                used[stage] = i;
                solve(stage + 1);
                visited[i] = 0;

    solve(0);
    print();








