from collections import deque

def findWarm(pos, visited, M, N):
    count = 0;
    queue = deque([]);
    # i==0 and j==0일 때 문제 발생
    for i in range(N):
        for j in range(M):
            subcount = 0;
            if visited[i][j]:
                continue;
            else:
                queue.append([j, i]);
                if pos[i][j] == 1:
                    visited[i][j] = True;
                    subcount += 1;
                while queue:
                    x, y = queue.popleft();
                    if x+1 < M and not visited[y][x+1]:
                        
                        if pos[y][x+1] == 1:
                            visited[y][x+1] = True;
                            queue.append([x+1,y]);
                            subcount += 1;
                    if x-1 >= 0 and not visited[y][x-1]:
                        
                        if pos[y][x-1] == 1:
                            visited[y][x-1] = True;
                            queue.append([x-1,y]);
                            subcount += 1;
                    if y-1 >= 0 and not visited[y-1][x]:
                        
                        if pos[y-1][x] == 1:
                            visited[y-1][x] = True;
                            queue.append([x,y-1]);
                            subcount += 1;
                    if y+1 < N and not visited[y+1][x]:
                        
                        if pos[y+1][x] == 1:
                            visited[y+1][x] = True;
                            queue.append([x,y+1]);
                            subcount += 1;
                if subcount > 0:
                    count += 1;
    return count;


T = int(input());
ans = [];
for tc in range(T):
    M, N, K = map(int, input().split());
    xyArr = [];
    pos = [];
    visited = [];

    for i in range(K):
        [x, y] = map(int, input().split());
        xyArr.append([x, y]);

    for i in range(N):
        pos.append([]);
        visited.append([]);
        for j in range(M):
            visited[i].append(False);
            if [j, i] in xyArr:
                pos[i].append(1);
            else:
                pos[i].append(0);
    ans.append(findWarm(pos, visited, M, N));
for i in ans:
    print(i);