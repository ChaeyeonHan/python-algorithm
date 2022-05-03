# NxM 공백으로 구분하여 입력받기
# 각 행에서 최솟값을 찾고, 그중에서 최댓값을 선택하기
N, M = map(int,input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)  # 현재 행에서 가장 작은수 찾기. min()함수 이용
    result = max(result, min_value)  # 그중에서 가장 큰수 찾기

print(result)