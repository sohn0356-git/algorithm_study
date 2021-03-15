# N과 M (10)

def pandc(num):
    global N, M, used, noneuse, visited, dd;
    if num >= M:
        for u in used:
            print(u, end=' ');
        print();
        return;
    for i in range(N):
        if visited[i] == 0:
            if num > 0:
                if used[num - 1] > noneuse[i]:
                    continue;
            visited[i] = 1;
            used[num] = noneuse[i];
            if (num >= M - 1):
                if dd.get(tuple(used)):
                    visited[i] = 0;
                    continue;
                else:
                    dd[tuple(used)] = 1;
            pandc(num + 1);
            visited[i] = 0;

N, M = map(int, input().split());
noneuse = sorted(list(map(int, input().split())));
used = [0] * M;
visited = [0] * N;
dd = dict();
pandc(0);
