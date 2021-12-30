K = int(input())
numbers=[0]*(K)
for i in range(K):
    num = int(input())
    if num == 0:
        numbers.pop()  # 바로 앞에 있는 원소 지우기
    elif num != 0:
        numbers.append(num)

print(sum(numbers))
