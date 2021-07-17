def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)