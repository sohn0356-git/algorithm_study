# N과 M (12)

def pandc(num):
    global N, M, used, noneuse, dd;
    if num >= M:
        for u in used:
            print(u, end=' ');
        print();
        return;
    for i in range(len(noneuse)):
        if num > 0:
            if used[num - 1] > noneuse[i]:
                continue;
        used[num] = noneuse[i];
        if (num >= M - 1):
            if dd.get(tuple(used)):
                continue;
            else:
                dd[tuple(used)] = 1;
        pandc(num + 1);

N, M = map(int, input().split());
noneuse = sorted(set(map(int, input().split())));
used = [0] * M;
dd = dict();
pandc(0);
