def pandc(num):
    global N, M, used, noneuse;
    if num >= M:
        for u in used:
            print(u, end=' ');
        print();
        return;
    for i in range(N):
        if num > 0:
            if used[num - 1] > noneuse[i]:
                continue;
        used[num] = noneuse[i];
        pandc(num + 1);

N, M = map(int, input().split());
noneuse = sorted(list(map(int, input().split())));
used = [0] * M;

pandc(0);