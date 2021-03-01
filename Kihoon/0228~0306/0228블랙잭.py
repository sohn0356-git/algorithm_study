# N = 카드 개수 (3 ≤ N ≤ 100)
# M = 카드에 쓰인 수 (10 ≤ M ≤ 300,000)

N,M = map(int, input().split(' '))
card = list(map(int, input().split(' ')))
result = 0;

for i in range(N):
    for j in range(i+1,N):
        for k in range(j + 1, N):
            if card[i]+card[j]+card[k] > M:
                continue
            else:
                result = max(result, card[i]+card[j]+card[k])


print(result)