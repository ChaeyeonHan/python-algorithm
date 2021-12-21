# 첫번째
N = int(input())

numbers = list(map(int, input().split()))
max = min = numbers[0]

for i in range(N):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]

print(min, max)


# 두번째

N = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))