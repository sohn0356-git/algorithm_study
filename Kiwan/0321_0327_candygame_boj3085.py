# 사탕 게임
def swap(x1, y1,x2, y2):
    global candy;
    temp = candy[y1][x1];
    candy[y1][x1] = candy[y2][x2];
    candy[y2][x2] = temp;

def bomboni(N):
    global candy, maxcnt;
    i = 0; j = 0;
    while i < N:
        while j < N:
            xx = j; yy = i; cnt = 0;
            # 1. 가로로 swap하고 탐색 - 가로 swap 시 세로탐색은 두번 (i,j), (i,j+1)
            if j < N - 1: # 가로 마지막 제외
                swap(j, i, j + 1, i); # swap
                # 가로탐색
                while xx < N - 1:
                    if candy[yy][xx] == candy[yy][xx + 1]:
                        cnt += 1; xx += 1;
                    else:
                        break;
                xx = j;
                while xx > 0:
                    if candy[yy][xx] == candy[yy][xx - 1]:
                        cnt += 1; xx -= 1
                    else:
                        break;
                if maxcnt < cnt:
                    maxcnt = cnt;
                cnt = 0; xx = j;
                # 세로탐색
                while yy < N - 1:
                    if candy[yy][xx] == candy[yy + 1][xx]:
                        cnt += 1; yy += 1;
                    else:
                        break;
                yy = i;
                while yy > 0:
                    if candy[yy][xx] == candy[yy - 1][xx]:
                        cnt += 1; yy -= 1;
                    else:
                        break;
                if maxcnt < cnt:
                    maxcnt = cnt;
                cnt = 0; yy = i;
                if xx + 1 < N - 1:
                    while yy < N - 1:
                        if candy[yy][xx + 1] == candy[yy + 1][xx + 1]:
                            cnt += 1; yy += 1;
                        else:
                            break;
                    yy = i;
                    while yy > 0:
                        if candy[yy][xx + 1] == candy[yy - 1][xx + 1]:
                            cnt += 1; yy -= 1;
                        else:
                            break;
                    if maxcnt < cnt:
                        maxcnt = cnt;
                    cnt = 0; yy = i;
                swap(j, i, j + 1, i); # swap 복구
            # 2. 세로로 swap하고 탐색 - 세로는 (i, j), (i+1, j) 탐색
            if i < N - 1: # 세로 마지막 제외
                swap(j, i, j, i + 1);  # swap
                # 가로탐색
                while xx < N - 1:
                    if candy[yy][xx] == candy[yy][xx + 1]:
                        cnt += 1;
                        xx += 1;
                    else:
                        break;
                xx = j;
                while xx > 0:
                    if candy[yy][xx] == candy[yy][xx - 1]:
                        cnt += 1;
                        xx -= 1
                    else:
                        break;
                if maxcnt < cnt:
                    maxcnt = cnt;
                cnt = 0; xx = j;
                if yy + 1 < N - 1:
                    while xx < N - 1:
                        if candy[yy + 1][xx] == candy[yy + 1][xx + 1]:
                            cnt += 1;
                            xx += 1;
                        else:
                            break;
                    xx = j;
                    while xx > 0:
                        if candy[yy + 1][xx] == candy[yy + 1][xx - 1]:
                            cnt += 1;
                            xx -= 1
                        else:
                            break;
                    if maxcnt < cnt:
                        maxcnt = cnt;
                    cnt = 0; xx = j;
                # 세로탐색
                while yy < N - 1:
                    if candy[yy][xx] == candy[yy + 1][xx]:
                        cnt += 1;
                        yy += 1;
                    else:
                        break;
                yy = i;
                while yy > 0:
                    if candy[yy][xx] == candy[yy - 1][xx]:
                        cnt += 1;
                        yy -= 1;
                    else:
                        break;
                if maxcnt < cnt:
                    maxcnt = cnt;
                cnt = 0; yy = i;
                swap(j, i, j, i + 1);  # swap 복구
            j += 1;
        i += 1; j = 0;

N = int(input());
candy = [];
for i in range(N):
    tmpStr = input();
    tmpCh = [];
    for j in range(N):
        tmpCh.append(tmpStr[j]);
    candy.append(tmpCh);
maxcnt = 0;
bomboni(N);
print(maxcnt + 1);