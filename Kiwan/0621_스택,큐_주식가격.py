## 주식가격

# prices = [1, 2, 3, 2, 3]
# def solution(prices):
#     n = len(prices)
#     answer = [0] * n

#     time = 0
#     while True:
#         time += 1
#         if time >= n:
#             break
#         for i, price in enumerate(prices):
#             if i < time:
#                 if price != 0:
#                     if price <= prices[time-1]:
#                         answer[i] += 1
#                     else:
#                         prices[i] = 0

#     return answer
# print(solution(prices))

# 다른사람 풀이
# def solution(prices):
#     answer = [0]*len(prices)
#     stack = []
 
#     for i, price in enumerate(prices):
#         #stack이 비었이면 false
#         while stack and price < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
 
#     # for문 다 돌고 Stack에 남아있는 값들 pop
#     while stack:
#         j = stack.pop()
#         answer[j] = len(prices) - 1 - j
 
#     return answer

# print(solution(prices))

def solution(prices):
    N = len(prices)
    stack = []
    answer = [0]  * N
    for i in range(N):
        if stack == []:
            stack.append((i, prices[i]))
        else:
            if stack[-1][1] <= prices[i]:
                stack.append((i, prices[i]))
            else:
                while stack and stack[-1][1] > prices[i]:
                    idx, price = stack.pop()
                    answer[idx] = i - idx
                stack.append((i, prices[i]))
    # print(stack)
    # print(answer)
    while stack:
        idx, price = stack.pop()
        answer[idx] = (N - 1) - idx
    # print(answer)
    return answer

# prices = [1,2,3,2,3]
# print(solution(prices))
# prices = [1,1,1,1,1]
# print(solution(prices))
# prices = [1,2,3,4,5]
# print(solution(prices))
# prices = [1,10,8,3,2,5]
# print(solution(prices))
prices = [100,10,100,10,100,11]
print(solution(prices))