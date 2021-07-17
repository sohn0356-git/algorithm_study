## 단어 변환

from collections import deque

def compSpell(word1, word2):
    chk = 0
    n = len(word1)
    for i in range(n):
        if word1[i] != word2[i]:
            chk += 1
    return chk

def solution(begin, target, words):
    answer = 0
    q = deque()
    if target in words:
        q.append([0, begin])
        while q:
            depth, word = q.popleft()
            if word == target:
                answer = depth
                break
            for i, next_word in enumerate(words):
                if compSpell(word, next_word) == 1:
                    q.append([depth+1, next_word])

    return answer
print(solution("hit", "cog", ["hot", "lot", "loe", "dog", "dot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "lot", "dog", "dot", "log", "cog"]))