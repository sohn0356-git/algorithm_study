# a b c 는 2,147,483,647이라는 숫자내에서 나옴 21억...
# 시간은 0.5초이니 10**8 = 100,000,000/2 5천만내외로 돌아야함
# 곱셈의 갯수를 줄여준다
# 재귀함수를 사용한다...(여기까지 생각 성공)

# 실패해서 구글링을 통해 방법 확인..
# b를 짝수일때와 홀수일때로 나누고 짝수이면 (b//2)**2 식으로 곱셈의 수를 줄임
# 예시 10**10 b 짝수-> (10**5)**2
# 예시 10**11 b 홀수-> (10**5)**2*10
#분할정복 문제라고 함
#시간복잡도는 log(b)
#공간복잡도는 <=c

def solve(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b%2==1:
        print(b)
        return solve(a,b-1)*a
    print(b)
    result = solve(a,b//2)
    result %=c
    return (result**2)%c

a, b, c = map(int,input().split())
print(solve(a,b)%c)

map(int,input().split())


