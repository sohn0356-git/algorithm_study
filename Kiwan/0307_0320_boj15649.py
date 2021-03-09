# N과 M 다시 풀기 (복습)

def pandc(num, N, M):
    global visited, used;
    if num >= M:
        for i in used:
            print(i, end=' ');
        print();
    for j in range(1, N+1):
        if visited[j] == 0 and len(used) < M:
            if used == []:
                visited[j] = 1;
                used.append(j);
                pandc(len(used), N, M);
                used.pop();
                visited[j] = 0;
            else:
                # if j > used[-1]:
                visited[j] = 1;
                used.append(j);
                pandc(len(used), N, M);
                used.pop();
                visited[j] = 0;

N, M = map(int, input().split());
visited = [0] * (N+1);
used = [];
pandc(0, N, M);
