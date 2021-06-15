def solution(participant, completion):
    answer = ''
    runner = {}
    for p in participant:
        if runner.get(p):
            runner[p] += 1
        else:
            runner[p] = 1
    for c in completion:
        runner[c] -= 1
    
    for k, v in runner.items():
        if v!=0:
            answer = k
    return answer
