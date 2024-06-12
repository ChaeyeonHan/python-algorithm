from collections import defaultdict
from itertools import combinations

# lower bound : 이진탐색에서 원하는 값 이상이 처음 나오는 위치
def lower_bound(start, end, target_list, target):
    if start >= end:
        return start
    mid = (start+end) // 2
    if target_list[mid] >= target:
        return lower_bound(start, mid, target_list, target)
    else:
        return lower_bound(mid+1, end, target_list, target)


def solution(infos, queries):
    answer = []
    # 언어/직군/경력/소울푸드를 key, 점수 리스트를 value로 갖는 딕셔너리
    dic = defaultdict(list)
    for info in infos:
        info = info.split(' ')
        condition = info[0:-1]  # 점수를 제외한 조건
        score = int(info[-1])
        for i in range(0, 5):
            # 앞의 4개의 요소들에서 i개를 뽑는 조합 생성
            # 뽑은 숫자에 해당하는 idx는 -로 조건 변경
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = '-'  # 조건변경
                key = ''.join(tmp)
                dic[key].append(score)
    for value in dic.values():
        value.sort()

    for query in queries:
        # 조건에 and 제거 & 공백 기준 나누기
        query = query.replace('and', '')
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0

        if target_key in dic:
            target_list = dic[target_key]
            # lower bound : 이진탐색에서 원하는 값 이상이 처음 나오는 위치
            idx = lower_bound(0, len(target_list), target_list, target_score)
            count = len(target_list)-idx
        answer.append(count)
    return answer