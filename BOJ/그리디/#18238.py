word = list(input())
count = 0
start = 'A'  # A부터 시작

for i in word:  # left와 right로 시계,반시계 방향 모두 계산해준다
    left = ord(i)-ord(start)
    right = ord(start)-ord(i)
    # 음수라면 알파벳 갯수인 26만큼 더해준다(원칸이 총 26개임)
    if left < 0:
        left += 26
    elif right < 0:
        right += 26
    count += min(left, right)  # 더 작은값을 더해준다
    start = i  # 시작점 이동

print(count)