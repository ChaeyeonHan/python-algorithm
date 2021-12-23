N = int(input())
times = list(map(int, input().split()))

times.sort()
# a = sorted(times)

result = 0
for i in range(N):
    result += times[i] * (N-i)
print(result)