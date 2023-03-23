import sys
input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    start, end = map(int, input().split())
    times.append([start, end])

times.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last_end = 0

for start, end in times:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)