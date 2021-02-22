# Bacjjoon 11021번
# 두 정수 A와 B를 입력 받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a = int(input());

for i in range(1,a+1):
    num1,num2 = map(int, input().split());
    print("Case #%d: %d" %(i, num1+num2));
