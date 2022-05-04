N = int(input())

height=[]
for _ in range(N):
    height.append(int(input()))

result = 1  # 보이는 갯수(오른쪽은 무조건 보임)
max_height = height[-1]

#for i in range(len(height)-1, -1, -1):
for i in reversed(range(N)):
    if height[i] > max_height:
        max_height = height[i]
        result += 1

print(result)