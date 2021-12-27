def hansu(num):
    count = 0
    for i in range(1, num+1):
        # 숫자를 자릿수를 기준으로 나누기!
        # str(n) : 숫자를 문자열로
        # map(int, str(n)) : 문자열로 된 각 자리수를 정수로 바꿔준다. "123" -> 정수 1, 2, 3
        num_list = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            count += 1
    return count

num = int(input())
print(hansu(num))