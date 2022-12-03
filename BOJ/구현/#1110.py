N = int(input())
num = N
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = b*10 + c
    count += 1
    if (num == N):
        break

# while True:
#     sum = (num // 10) + (num % 10)
#     new_num = (num % 10) * 10 + (sum % 10)
#     count += 1
#     if (new_num == num):
#         break
# 이건 시간초과가 난다..

print(count)
