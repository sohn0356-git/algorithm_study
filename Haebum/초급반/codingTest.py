#재귀함수
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


#실행문
factorial(4)

실행하게되면 처음에
factorial(4) 를 실행해서 4*factorial(3) 을 리턴받게 된다.

리턴받은 factorial(3)은 다시 3*factorial(2)를 리턴받고
factorial(2)는 2*factorial(1)을 리턴.

factorial(1)은 탈출조건인 if n==1을 성립하면서
더 이상 factorial함수를 부르지않고 1로 리턴된다.

그럼 4*3*2*1이 남게 되어 답은 24가 된다.

4*factorial(3) 일때 factorial(3)의 자리에 3*factorial(2)가 들어간다고 보면 된다.
