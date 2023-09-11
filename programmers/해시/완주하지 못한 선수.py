# 이름을 키로 사용, 통명이인의 수를 값으로
def solution(participant, completion):
    dict = {}
    for i in participant:
        dict[i] = dict.get(i, 0) + 1  # 주어진 키 i가 존재하면 그 값을, 없으면 0을
    for i in completion:
        dict[i] -= 1
    result = [k for k, v in dict.items() if v > 0]
    return result[0]