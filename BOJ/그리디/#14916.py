import sys
input = sys.stdin.readline

N = int(input())
result = 0

while True:
    if N % 5 == 0:
        result += N//5
        break
    else:  # 나누어 떨어지지 않는다면 2씩 빼준다
        N -= 2
        result += 1
    if N < 0:
        break

if N < 0:
    print(-1)
else:
    print(result)