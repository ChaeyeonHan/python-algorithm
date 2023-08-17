import sys
input = sys.stdin.readline

N = int(input())
pillar = []
for _ in range(N):
    a, b = map(int, input().split())
    pillar.append((a, b))

pillar.sort(key=lambda x:x[0])  # x축 기준으로 정렬

idx = 0
result = 0
for i in range(N):  # 최대 높이의 idx 찾기
    if pillar[i][1] > result:
        result = pillar[i][1]
        idx = i

# 왼쪽부분
height = pillar[0][1]
for i in range(idx):
    if pillar[i+1][1] > height:  # 앞에 있는 기둥보다 높다면
        result += height * (pillar[i+1][0]-pillar[i][0])
        height = pillar[i+1][1]
    else:
        result += height * (pillar[i+1][0]-pillar[i][0])

# 오른쪽부분(뒤에서부터 한개씩 진행)
height = pillar[N-1][1]  # 가장 오른쪽 높이
for i in range(N-1, idx, -1):
    if pillar[i-1][1] > height:
        result += height *(pillar[i][0]-pillar[i-1][0])
        height = pillar[i-1][1]
    else:
        result += height*(pillar[i][0]-pillar[i-1][0])
print(result)
