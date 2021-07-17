#풀이방식 3     자리수는 무궁무진하게 늘어날 수 있으므로 이런 풀이는 어떨까요?
num1 = int(input())
num2 = int(input())
ans = num1*num2
while num2>0:
    print(num1*(num2%10))
    num2 = num2 // 10
print(ans)
