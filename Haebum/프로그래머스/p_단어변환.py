#bfs 사용
# begin과 한자리만 다르면서 word를 확인하여 변경
# bfs에 변경중인 단어를 넣고 체크
# 현재 체크한 변경횟수가 정답보다 작으면 정답으로 체인지.
# 한번도 바뀌지 않았으면 0으로 반환

from collections import deque
import math

def solution(begin, target, words):
    #초기값을 무한으로 지정
    answer = math.inf
    #사용한 언어인지 아닌지 체크
    visited = [0] * len(words)

    queue = deque()
    count = 0 # 변경횟수
    queue.append([begin,count])
    while(queue):
        cur,count = queue.popleft()
        #현재가 타겟일때
        if cur == target:
            #최소횟수라면 정답으로 변경
            if answer > count:
                answer = count

        for idx,word in enumerate(words): # 50개
            position = 0
            for j in range(len(word)): #10
                #알파벳 각 자리 맞는 갯수 체크
                if visited[idx] == 0 and word[j] == cur[j]:
                    position += 1
            # 한자리만 변경되었다면
            if position == len(cur) -1:
                visited[idx] = 1
                queue.append([words[idx],count+1])
    #타겟이 나오지 않는 경우
    if answer == math.inf:
        answer = 0

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
solution(begin, target, words)