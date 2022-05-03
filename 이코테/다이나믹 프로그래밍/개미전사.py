N = int(input())
nums = list(map(int, input().split()))

# 계산결과를 저장하기 위한 배열
d = [0]*100

d[0] = nums[0]
d[1] = max(nums[0], nums[1])

for i in range(2,N):
    d[i] = max(d[i-1], d[i-2] + nums[i]) # 누적값+자기자신과 자기자신 바로 앞의 값을 비교해서 큰값 고르기

print(d[N-1])