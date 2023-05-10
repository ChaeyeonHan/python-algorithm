import sys
input = sys.stdin.readline

n = int(input())

# 리스트의 각 요소를 0으로 할당해두고, 값을 입력받을 때마다 해당 값의 인덱스에 +1씩 해준다
result = [0] * 10001

for _ in range(n):
    result[int(input())] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)