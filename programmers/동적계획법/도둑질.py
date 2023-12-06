def solution(money):
    dp1 = [0] * len(money)  # 1번 집을 터는 경우
    dp2 = [0] * len(money)  # 1번 집을 털지 않는 경우
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)-1):
        dp1[i] = max(money[i]+dp1[i-2], dp1[i-1])
    for i in range(2, len(money)):
        dp2[i] = max(money[i]+dp2[i-2], dp2[i-1])
    return max(max(dp1), max(dp2))