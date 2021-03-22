from collections import deque;

def bfs(start):
    global N, visited;
    queue = deque([[0, 1, 1, 0]]);
    while queue:
        num, a, m, b = queue.popleft(); # num:연산 횟수, a:액션, m:화면에 이모티콘수, b:버퍼에 이모티콘 개수
        visited[(num, a, m, b)] = 1;
        if a == 1:
            m += b;
        elif a == 2:
            b = m;
        else:
            m -= 1;
        if a == 1 and m >= N:
            return num;
        if m < 0:
            continue;
        # 1.출력(클립보드->화면) / 2.저장(화면->클립보드) / 3.삭제(화면에 이모티콘 1개 삭제)
        if visited.get((num + 1, 1, m, b)) != 1:
            queue.append([num + 1, 1, m, b]);
        if visited.get((num + 1, 2, m, b)) != 1:
            queue.append([num + 1, 2, m, b]);
        if visited.get((num + 1, 3, m, b)) != 1:
            queue.append([num + 1, 3, m, b]);

N = int(input());
visited = dict();
print(bfs(0));