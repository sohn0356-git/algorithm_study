def solution(N, number):
    answer = -1
    dp = []
    
    for i in range (1,9):
        all_case = set()
        check_number = int(str(N) * i)
        # {N}, {NN} , {NNN}...
        all_case.add(check_number)
        
        for j in range(0,i-1): #i-1 =2   0,1,2
        #j 개를 사용해서 만든 값들
            for op1 in dp[j]: # dp[j] =  0,1,2
                for op2 in dp[-j-1] : #dp[-j-1] = -1, -2, -3 -> dp의 2, 1, 0
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
        # dp [1] = 원소의 개수 1
        # dp [2] = 1*4 + 1
        # dp [3] = (1*4 + 1)
        # dp [4] = (5*4) + 1
        if number in all_case:
            answer = i
            break
            
        dp.append(all_case) 
        

    return answer

N = 5
number = 12
solution(N, number)