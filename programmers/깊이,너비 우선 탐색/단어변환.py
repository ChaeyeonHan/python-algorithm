from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    V = [0] * len(words)  # 방문여부 확인 리스트
    while queue:
        word, cnt = queue.popleft()  # [단어, 바꾼 횟수]
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:  # 확인 안한 단어라면
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:  # 한글자만 다르다면
                    queue.append([words[i], cnt+1])
                    V[i] = 1

    return answer