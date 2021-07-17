## K번째수
def solution(array, commands):
    answer = []
    
    for command in commands:
        temp = sorted(array[(command[0]-1):command[1]])[command[2]-1]
        answer.append(temp)
        
    return answer