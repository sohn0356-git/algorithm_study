
s = []
temp = []
k = []
temp = list(map(int, input().split(' ')))
while temp[0] != 0:
    k.append(temp[0])
    s.append(temp[1:])
    temp = list(map(int, input().split(' ')))
# 몇 번째 수를 선택했는지 기록
used = [[0]*6 for _ in range(len(s))]
# 방문 여부 체크
visited = [[0]*k[i] for i in range(len(s))]

def solve(stage):
    if stage == 6:
        for i in range(6):
            print(lotto[u[i]], end=' ')
        print()
        return
    for i in range(0,len(lotto)):
        if stage > 0:           # stage가 0보다 크면(숫자를 한개 이상 선택했으면)
            if i <= u[stage-1]: # 현재 숫자가 이전에 선택한 숫자보다 작거나 같으면
                continue        # 선택하지 않고 다음으로 넘어간다
        if v[i] == 0:           # 현재 숫자를 사용하지 않았으면
            v[i] = 1            # 사용했다고 표시
            u[stage] = i        # 현재 stage에 i를 선택했다고 표시
            solve(stage+1)      # 재귀함수호출로 다음 stage로 이동
            v[i] = 0            # 사용하고 나서는 반납

for i in range(len(s)):
    lotto = s[i]
    u = used[i]
    v = visited[i]
    solve(0) # i : 줄 번호
    print()