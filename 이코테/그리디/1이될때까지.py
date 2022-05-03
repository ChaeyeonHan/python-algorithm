'''
내가 푼거
N, K = map(int, input().split())
count = 0

while True:
    if (N % K) == 0:
        count += 1
        N = N // K
        if N == 1:
            print(count)
            break
    else:
        N -= 1
        count += 1
'''

n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
