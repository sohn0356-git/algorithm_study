
# 1~n 중에 m개의 수를 뽑아 수열을 만든다.

n, m = map(int, input().split());

used = [0] * m;
visited = [0] * n;
card = [];

for i in range(1, n+1) :
    card.append(i);

def solve(stage) :
    if stage == m :  # 원하는만큼 다 뽑았으면 출력하자.
        for i in used :
            print(card[i], end = ' ');
        print();
        return

    for i in range(n) : # 주어진 것들에 뭘 뽑을지
        if visited[i] == 0 :
            visited[i] = 1;
            used[stage] = i;
            solve(stage + 1);
            visited[i] = 0;

solve(0);
