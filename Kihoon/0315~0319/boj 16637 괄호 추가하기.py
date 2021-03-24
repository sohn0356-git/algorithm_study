# 괄호 추가하기
from collections import deque;

def calc(a, op, b):
    if op == '+':
        return int(a) + int(b);
    elif op == '-':
        return int(a) - int(b);
    elif op == '*':
        return int(a) * int(b);

def result(visited):
    global str;
    queue = deque();
    idx = 0;
    for _ in str:
        if _.isnumeric():
            if visited[idx] == 1:
                op = queue.pop();
                a = queue.pop();
                queue.append(calc(a, op, _));
            else:
                queue.append(int(_));
        else:
            idx += 1;
            queue.append(_);
    # print(queue);
    while queue:
        try:
            a = queue.popleft();
            op = queue.popleft();
            b = queue.popleft();
            queue.appendleft(calc(a, op, b));
        except:
            return a;

def selopr(num):
    global opr, visited, N, str, lenopr, res;
    # print(visited, end=' ');
    res.append(result(visited));
    for i in range(1, lenopr + 1):
        if visited[i] == 0:
            if i < lenopr:
                if visited[i - 1] != 0 or visited[i + 1] != 0:
                    continue;
            else:
                if visited[i - 1] != 0:
                    continue;
            visited[i] = 1;
            selopr(num + 1);
            visited[i] = 0;

N = int(input());
str = input();
visited = [0] * (int(N / 2) + 1);
opr = [];
num = [];
res = [];
for _ in str:
    if not _.isnumeric():
        opr.append(_);
    else:
        num.append(_);

lenopr = len(opr);
# print(opr, len(opr));
# print(visited, len(visited));
selopr(0);
print(max(res));