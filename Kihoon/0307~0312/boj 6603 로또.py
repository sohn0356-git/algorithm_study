S = [];
k=1;
used = []
visited = []

def lotto(stage):
    if stage == 6:
        for i in used:
            print(S[i], end=' ');
        print();
        return

    for i in range(k):
        if stage > 0 and i <= used[stage - 1]:
            continue
        if visited[i] == 0:
            visited[i] = 1;
            used[stage] = i;
            lotto(stage + 1);
            visited[i] = 0;


while k!=0: # <- 덮어 씌워짐
    S = list(map(int, input().split()));
    k = S[0];
    if k==0:
        break;
    S.remove(k)

    # for i in range(k):
    #     S.append(numbers[i])
    #S.sort()

    used = [0]*6
    visited = [0]*50

    lotto(0)
    print()



