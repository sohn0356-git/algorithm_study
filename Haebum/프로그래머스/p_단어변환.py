#bfs 사용
# begin과 한자리만 다르면서 word를 확인하여 변경
# bfs에 변경중인 단어를 넣고 체크
# 현재 체크한 변경횟수가 정답보다 작으면 정답으로 체인지.
# 한번도 바뀌지 않았으면 0으로 반환

from collections import deque
import math

def solution(begin, target, words):
    answer = math.inf
    visited = [0] * len(words)

    queue = deque()
    count = 0
    queue.append([begin,count])
    while(queue):
        cur,count = queue.popleft()
        if cur == target:
            if answer > count:
                answer = count

        for idx,word in enumerate(words): # 50개
            position = 0
            for j in range(len(word)): #10
                if visited[idx] == 0 and word[j] == cur[j]:
                    position += 1
            if position == len(cur) -1:
                visited[idx] = 1
                queue.append([words[idx],count+1])
    
    if answer == math.inf:
        answer = 0

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
solution(begin, target, words)