# %연산자를 적극 활용해 보는 건 어떨까요?

h, m = map(int,input().split())

if m < 45:
    h = (h + 23) % 24
m = (m + 15) % 60

print(h, m)