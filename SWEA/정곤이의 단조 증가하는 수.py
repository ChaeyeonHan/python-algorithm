def checkIncr(num):
    str_list = str(num)
    for i in range(len(str_list)-1):
        if str_list[i] > str_list[i+1]:
            return False
    return True

T = int(input())
for t in range(1, T+1):
    result = -1
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)-1):
            temp = numbers[i] * numbers[j]
            if checkIncr(temp) and result < temp:
                result = temp
    print(f'#{t} ' + str(result))