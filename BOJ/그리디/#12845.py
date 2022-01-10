# 내가 푼거
N = int(input())  # 카드 수
level = list(map(int, input().split()))

max_level = max(level)  # 최대 레벨 찾기
count = 0
# 처음 계산시 최대레벨카드에 덧붙여야 계속 높은 레벨 유지 가능
for i in range(len(level)):
    count += level[i]
count += (len(level)-2) * max_level  # 최대레벨은 (n-2)번만큼 더하기
print(count)


# 참고해서 다시 푼거
N = int(input())  # 카드 수
level = list(map(int, input().split()))

level.sort(reverse=True)
count = 0  # 골드 카운트할 변수

for i in range(len(level)):
    if i <= 1:  # 처음에 카드 합칠때
        count += level[i]
    else:  # 기존 골드 + 새로 추가된 골드
        count += level[0] + level[i]

print(count)