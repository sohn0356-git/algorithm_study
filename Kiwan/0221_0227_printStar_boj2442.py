# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
#
# 별은 가운데를 기준으로 대칭이어야 한다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

lineNum = int(input());

for i in range(1, lineNum+1):
    for j in range(lineNum - i):
        print(' ', end='');
    for k in range(i):
        print('*', end='');
    for l in range(k):
        print('*', end='');
    print('');

