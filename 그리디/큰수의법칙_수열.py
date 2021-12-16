N, M, K = map(int, input().split())

a = list(map(int, input().split()))

a.sort()
max_first = a[N-1]
max_second = a[N-2]

# 가장 큰수가 몇번 더해지는지 구하기
count = int(M/(K+1)) * K
count += M % (K+1)

result = 0
result += count * max_first
result += (M-count) * max_second

print(result)