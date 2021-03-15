def pandc(num):
    global N, M, used, noneuse;#, visited;
    if num >= M:
        for u in used:
            print(u, end=' ');
        print();
        return;
    for i in range(N):
        used[num] = noneuse[i];
        pandc(num + 1);

N, M = map(int, input().split());
noneuse = sorted(list(map(int, input().split())));
#visited = [0] * N;
used = [0] * M;

pandc(0);