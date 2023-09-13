def solution(clothes):
    dict = {}
    for name, type in clothes:
        dict[type] = dict.get(type, 0) + 1
    answer = 1
    for type in dict:
        answer *= (dict[type]+1)
    return answer-1