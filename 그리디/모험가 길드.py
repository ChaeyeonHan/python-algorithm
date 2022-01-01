N = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0  # 현재 그룹의 모험가 카운트
result = 0  # 가능한 그룹수 카운트
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0  # 모험가 수 초기화

print(result)