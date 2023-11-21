for t in range(1, 11):
    test_num = int(input())
    numbers = list(map(int, input().split()))
    while numbers[-1] > 0:
        for i in range(1, 6):
            if numbers[0] - i > 0:  # 감소시킨 뒤 0보다 크면
                numbers.append(numbers[0] - i)
                numbers.pop(0)
            else:
                numbers.append(0)
                numbers.pop(0)
                break
    print(f'#{t}', *numbers)
