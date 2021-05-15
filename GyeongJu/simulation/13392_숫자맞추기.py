import sys
sys.setrecursionlimit(100000)

def solve(stage, cum):
    global N, DP, cur, target

    if stage==N:
        return 0

    if DP[stage][cum]!=-1:
        return DP[stage][cum]
    
    int_cur = int(cur[stage])
    int_target = int(target[stage])
    int_cur += cum
    int_cur %= 10
    sub = int_target - int_cur
    
    # turn left
    if sub<0:
        sub += 10
    t1 = sub + solve(stage+1, (cum+sub)%10)

    # turn right
    sub = int_cur - int_target
    if sub<0:
        sub += 10
    t2 = sub + solve(stage+1, cum)

    res = min(t1,t2)
    return res


DP = [[-1]*10 for _ in range(10001)]

N = int(input())
cur = input()
target = input()

print(solve(0,0))
