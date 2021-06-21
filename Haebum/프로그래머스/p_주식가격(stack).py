def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices)-1-i)
    stack = []
    for cnt_time, price in enumerate(prices):
        while stack:
            if stack[-1][1] > price:
                answer[stack[-1][0]] = cnt_time - stack[-1][0]
                stack.pop()
            else:
                break
        stack.append([cnt_time, price])
    print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)