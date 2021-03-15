def pandc(num):
    global N, M, used, visited;
    if num >= M:
        for u in used:
            print(u, end=' ');
        print();
        return;
    for i in range(N):
        used[num] = i + 1;
        pandc(num + 1);

N, M = map(int, input().split());
visited = [0] * N;
used = [0] * M;

pandc(0);