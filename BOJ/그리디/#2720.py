'''
T = int(input())  # 테스트 개수
coins = [25, 10, 5, 1]

for i in range(T):
    C = int(input())  # 거스름돈 금액
    list = []
    for coin in coins:
        list.append(C//coin)
        C = C % coin
    print(*list)  # *는 [4,2,0,4]를 4,2,0,4로 출력시켜준다
'''

# 딕셔너리를 이용한 풀이
T = int(input())

for _ in range(T):
    money = int(input())
    coins = {25:0, 10:0, 5:0, 1:0}
    for num in [25, 10, 5, 1]:
        coins[num] += (money // num)  # 몫을 더해준다
        money = money % num
    print(coins[25], coins[10], coins[5], coins[1])