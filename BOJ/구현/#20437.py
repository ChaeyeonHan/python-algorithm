import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W = input().rstrip()
    K = int(input())
    alpha = {}  # 딕셔너리로 알파벳 카운트
    check = {}  # K번 이상 나오는 알파벳의 idx 저장
    ans = False
    for i in W:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1
    # print(alpha)
    for i in range(len(W)):
        if alpha[W[i]] < K:
            continue
        # key: 문자열, value: 해당 문자열의 idx / check.get(W[i], []) -> 해당 문자열이 없으면 None을 리턴해주기 위해(None, [])
        ans = True
        check[W[i]] = check.get(W[i], []) + [i]

    # print(check)  # {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]}

    max_pos, min_pos = -1, len(W)
    for key, value_list in check.items():  # 딕셔너리 모두 돌면서
        for i in range(len(value_list)-K+1):
            max_pos = max(max_pos, value_list[i+K-1] - value_list[i]+1)
            min_pos = min(min_pos, value_list[i+K-1] - value_list[i]+1)
    if ans:
        print(min_pos, max_pos)
    else:
        print(-1)