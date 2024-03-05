def solution(enroll, referral, seller, amount):
    # 판매원 이름, 참여시킨 다른 판매원 이름, 판매원 이름 & 판매량

    money = [0 for _ in range(len(enroll))]

    dict = {}  # 이름, 인덱스
    for i, e in enumerate(enroll):  # enroll에 있는 사람 순서대로 얻는 이익 출력
        dict[e] = i
    for s, a in zip(seller, amount):
        profit = a * 100
        while profit > 0 and s != "-":
            idx = dict[s]  # 해당 사람의 인덱스 번호
            money[idx] += profit - profit // 10  # 10프로를 제외하고 얻는 이익
            profit //= 10
            s = referral[idx]

    return money