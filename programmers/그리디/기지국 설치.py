import math

def solution(n, stations, w):
    answer = 0
    marks = []

    before = 0
    for pos in stations:
        start, end = max(pos-w, 1), min(pos+w, n)
        if not before:  # 처음 시작하는 경우
            marks.append(start-1)
            before = end
        else:
            if before+1 < start:  # 안겹치는 경우
                marks.append(start-before-1)
            before = end

    marks.append(n-before)
    print(marks)
    for m in marks:
        if m > 0:
            answer += math.ceil(m/(2*w+1))
            # print(answer)
    return answer

print(solution(11, [4, 11], 1))
# print(solution(16, [9], 2))