N, M = map(int, input().split())
total_apples = int(input())
position = []
for i in range(total_apples):
    position.append(int(input()))  # 사과 떨어지는 위치
# 바구니는 left는 1, right는 1+입력받은 바구니 사이즈이다.

count = 0
size = M
left = 1
right = left + size - 1

for i in range(len(position)):
    if left <= position[i] <= right:  # 사과가 바구니에 들어간다
        continue
    if (position[i] > right):
        temp = position[i]-right
        left += temp
        right += temp
        count += temp
    if (position[i] < left):
        temp = left-position[i]
        left -= temp
        right -= temp
        count += temp

print(count)
