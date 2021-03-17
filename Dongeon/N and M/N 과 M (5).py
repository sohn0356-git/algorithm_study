
n, m = map(int, input().split())

list1 = list(map(int, input().split()));
list1.sort()

used = [0] * m;
visited = [0] * n;

def solve(stage) :
    if stage == m :
        for i in used :
            print(list1[i], end=" ")
        print()
        return

    for i in range(n) :
        if visited[i] == 0 :
            visited[i] = 1;
            used[stage] = i;
            solve(stage +1)
            visited[i] = 0;

solve(0);




