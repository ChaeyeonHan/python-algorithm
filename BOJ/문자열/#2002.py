import sys
input = sys.stdin.readline

N = int(input())

in_cars = {}
out_cars = []

for i in range(N):
    a = input().rstrip()
    in_cars[a] = i
for _ in range(N):
    out_cars.append(input().rstrip())

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if in_cars[out_cars[i]] > in_cars[out_cars[j]]:
            cnt += 1
            break
print(cnt)