# N과 M (11)

def pandc(num):
    global N, M, used, noneuse;
    if num >= M:
        for u in used:
            print(u, end=' ');
        print();
        return;
    for i in range(len(noneuse)):
        used[num] = noneuse[i];
        pandc(num + 1);

N, M = map(int, input().split());
noneuse = sorted(set(map(int, input().split())));
used = [0] * M;
pandc(0);
