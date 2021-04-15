# 연구소1
import copy, collections;

# 벽세우기 함수
def makewall(wall):
    global N, M, mapp, max;
    if wall >= 3:
        # mapp 저장
        mappp = copy.deepcopy(mapp);
        # 바이러스 퍼뜨리기
        spreadvirus(mapp);
        # 안전영역 검사
        count = chksafezone(mapp);
        if max < count:
            max = count;
        # mapp 되돌리기
        mapp = copy.deepcopy(mappp);
        return max;
    # 벽 세우기
    for n in range(N):
        for m in range(M):
            if mapp[n][m] == 0:
                mapp[n][m] = 1;
                makewall(wall + 1);
                mapp[n][m] = 0;



# 바이러스 퍼뜨리기
def spreadvirus(mapp):
    global N, M;
    queue = collections.deque([]);
    dx = [-1, 0, 1, 0];
    dy = [0, 1, 0, -1];
    for n in range(N):
        for m in range(M):
            if mapp[n][m] == 2:
                queue.append([n, m]);
    while queue:
        n, m = queue.popleft();
        for i in range(4):
            mm = m + dx[i];
            nn = n + dy[i];
            if 0 <= nn < N and 0 <= mm < M and mapp[nn][mm] == 0:
                mapp[nn][mm] = 2;
                queue.append([nn, mm]);

# 안전영역 검사
def chksafezone(mapp):
    global N, M;
    count = 0;
    for n in range(N):
        for m in range(M):
            if mapp[n][m] == 0:
                count += 1;
    return count;

# 입력
N, M = map(int, input().split());       # N, M 입력 받기
mapp = [];                              # map 입력 받기
for _ in range(N):
    temp = list(map(int, input().split()));
    mapp.append(temp);
visited = [[-1] * M for _ in range(N)]; # 방문 여부 리스트
max = 0;                                # 최대 값 저장
makewall(0);
print(max);                             # 출력