# 완주하지 못한 선수
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
#     for i, player in enumerate(completion):
#         if player in participant:
#             participant.remove(player)
#     answer = participant.pop()
#     return answer
# print(solution(participant, completion))

# def solution(participant, completion):
#     answer = ''
#     players = dict()
#     idx = None
#     for i, player in enumerate(participant):
#         try:
#             players[player] += 1
#             idx = i
#             break
#         except:
#             players[player] = 1
#             if player not in completion:
#                 idx = i
#
#     answer = participant[idx]
#
#     return answer

# 통과....
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        try:
            if participant[i] != completion[i]:
                answer = participant[i]
                break
        except:
            answer = participant[i]
    return answer

print(solution(participant, completion))