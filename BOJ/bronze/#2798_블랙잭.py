# N은 카드 갯수, M은 넘지않는 최대 정수 M
N, M = map(int, input().split())
# d는 입력받는 카드 숫자
d = list(map(int, input().split()))
max = 0
sum = 0


# for문 3개로
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if(d[i]+d[j]+d[k] > M):
                continue # 해당되는 경우 X. 계속 진행
            else:
                sum = d[i]+d[k]+d[j]
                if(max <= sum):
                    max = sum

print(max)

# 정렬해서
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_n = 0

nums.sort()
for i in range(N-1, 1, -1):
    for j in range(i-1, 0, -1):
        for k in range(j-1, -1, -1):
            # print(i, j, k)
            sum = nums[i] + nums[j] + nums[k]
            if sum <= M and max_n < sum:
                max_n = sum  # sum값 갱신
print(max_n)