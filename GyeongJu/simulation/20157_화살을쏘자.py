def gcd(x, y):
    if x < y:
        x, y = y, x
    while y>0:
        x, y = y, x%y
    return x

ans = 1
N = int(input())
pos_grad = {}
neg_grad = {}

for i in range(N):
    x, y = map(int, input().split(' '))
    gcd_xy = gcd(abs(x), abs(y))
    x /= gcd_xy
    y /= gcd_xy

    if x>0:
        if pos_grad.get((x,y)):
            pos_grad[(x,y)] += 1
            if ans < pos_grad[(x,y)]:
                ans = pos_grad[(x,y)]
        else:
            pos_grad[(x,y)] = 1
    else:
        if neg_grad.get((x,y)):
            neg_grad[(x,y)] += 1            
            if ans < neg_grad[(x,y)]:
                ans = neg_grad[(x,y)]
        else:
            neg_grad[(x,y)] = 1
print(ans) 
