def pandc(num):
    global N, M, used, noneuse, visited, dd;
    for i in range(len(noneuse)):
        if visited[i] == 0:
            visited[i] = 1;
            used[num] = noneuse[i];
            if num >= M - 1:
                if dd.get(tuple(used)):
                    visited[i] = 0;
                    continue;
                else:
                    dd[tuple(used)] = 1;
                    for u in used:
                        print(u, end=' ');
                    print();
                    visited[i] = 0;
                    continue;
            else:
                pandc(num + 1);
                visited[i] = 0;

N, M = map(int, input().split());
noneuse = sorted(list(map(int, input().split())));
used = [0] * M;
visited = [0] * N;
dd = dict();

pandc(0);
