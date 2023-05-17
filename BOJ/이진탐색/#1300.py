import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

start, end = 0, N**2
answer = 0

# K보다 작은 수가 몇개인지 찾아서 K가 몇번째 숫자인지 찾아낸다
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, N+1):
        cnt += min(mid // i, N)
    if cnt >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)