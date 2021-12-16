N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # 가장 작은수들 중에서 가장 큰수 찾기
    result = max(result, min_value)

print(result)