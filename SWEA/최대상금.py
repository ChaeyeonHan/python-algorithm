T = int(input())

def dfs(count):
    global answer
    if count == 0:
        answer = max(int("".join(number)), answer)
        return
    # 숫자 바꾸기
    for i in range(length):
        for j in range(i+1, length):  # 현재자리(i) 다음자리부터 비교
            number[i], number[j] = number[j], number[i]
            temp = "".join(number)  # 합치기
            if visited.get((temp, count-1), 1):  # 딕셔너리에 없다면
                visited[(temp, count-1)] = 0
                dfs(count-1)
            number[i], number[j] = number[j], number[i]


for i in range(1, T+1):
    answer = 0
    number, exchange_times = input().split()
    number = list(number)
    exchange_times = int(exchange_times)

    length = len(number)
    visited = {}  # 앞에서 나온 수인지 확인하기 위한 딕셔너리
    dfs(exchange_times)
    print("#{} {}".format(i, answer))