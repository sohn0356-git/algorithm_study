"""
n 개 중 m 개를 선택해 수열을 만든다.
중복을 허용한다.
"""

n, m = map(int, input().split())

used = [0] * m
card = []
for i in range(1,n+1) :
    card.append(i)

def solve(stage) :
    if stage == m :
        for i in used :
            print(card[i], end = ' ' )
        print()
        return

    for i in range(n) :
            used[stage] = i;
            solve(stage + 1);
solve(0)