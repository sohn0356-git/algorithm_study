def watch(room, r, c, dir):
    global N, M, dirR, dirC
    nR = r + dirR[dir]
    nC = c + dirC[dir]
    while 0 <= nR and nR < N and 0 <= nC and nC < M:
        if room[nR][nC] == 6:
            break
        elif room[nR][nC] == 0:
            room[nR][nC] = 7
        nR += dirR[dir]
        nC += dirC[dir]

def cnt_room(room):
    global N, M ,cctv
    cnt = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == 0:
                cnt += 1
    return cnt

def solve(stage):
    global N, M, room, cctv, dirR, dirC, _room, answer
    if stage==len(cctv):
        for i in range(N):
            for j in range(M):
                _room[i][j] = room[i][j]
        for c in cctv.values():
            if _room[c[0]][c[1]] == 1:
                watch(_room, c[0], c[1], c[2])
            elif _room[c[0]][c[1]] == 2:
                watch(_room, c[0], c[1], c[2])
                watch(_room, c[0], c[1], (c[2]+2)%4)
            elif _room[c[0]][c[1]] == 3:
                watch(_room, c[0], c[1], c[2])
                watch(_room, c[0], c[1], (c[2]+3)%4)
            elif _room[c[0]][c[1]] == 4:
                watch(_room, c[0], c[1], c[2])
                watch(_room, c[0], c[1], (c[2]+2)%4)
                watch(_room, c[0], c[1], (c[2]+3)%4)
            elif _room[c[0]][c[1]] == 5:
                for d in range(4):
                    watch(_room, c[0], c[1], d)
        answer = min(answer, cnt_room(_room))
        return
    
    if room[cctv[stage][0]][cctv[stage][1]] == 1 or room[cctv[stage][0]][cctv[stage][1]] == 3 or room[cctv[stage][0]][cctv[stage][1]] == 4:
        for i in range(4):
            cctv[stage][2] = i
            solve(stage+1)
    elif room[cctv[stage][0]][cctv[stage][1]] == 2:
        for i in range(2):
            cctv[stage][2] = i
            solve(stage+1)
    else:
        solve(stage+1)

dirR = [0,-1,0,1]
dirC = [1,0,-1,0]
N, M = map(int, input().split())
room = [list(map(int ,input().split())) for _ in range(N)]
_room = [[0]*M for _ in range(N)]
cctv = {}
cctv_idx = 0
answer = 987654321

for i in range(N):
    for j in range(M):
        if room[i][j] > 0 and room[i][j] < 6:
            cctv[cctv_idx] = [i, j, 0]   #cctv위치, 방향
            cctv_idx += 1

solve(0)
print(answer)