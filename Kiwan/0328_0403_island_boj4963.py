
def island():
    global w, h, m, visited, cnt;
    for i in range(h):
        for j in range(w):
            posy = i; posx = j;
            if visited[posy][posx] == 0:
                if m[posy][posx] == 1:
                    cnt += 1;
                    count(posy, posx);
                else:
                    continue;
    return cnt;

def count(posy, posx):
    global visited, cnt;
    vec = [[1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1]];
    for y, x in vec:
        posy += y; posx += x;
        if posy < 0 or posx < 0 or posy >= h or posx >= w:
            posy -= y; posx -= x;
            continue;
        if visited[posy][posx] == 0:
            if m[posy][posx] == 0:
                visited[posy][posx] = -1;
                posy -= y; posx -= x;
                continue;
            else:
                visited[posy][posx] = cnt;
                count(posy, posx);
                posy -= y; posx -= x;
        else:
            posy -= y; posx -= x;


visited = None;
res = [];
while True:
    w, h = map(int, input().split());
    cnt = 0;
    if w == 0 or h == 0:
        break;
    visited = [[0] * w for _ in range(h)]
    m = [];
    temp = [];
    for _ in range(h):
        temp = list(map(int, input().split()));
        m.append(temp);
    #res.append(island());
    print(island());
for _ in res:
    print(_);