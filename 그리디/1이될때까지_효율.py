#  교재 102쪽 잘 이해가 안됨.... 미완!!!
N, K = map(int, input().split())
result = 0

while True:
    target = (N // K) * K
    result += (N-target)
    N = target
    if (N < K):
        break
    result += 1
    N //= K

result += (N-1)
print(result)