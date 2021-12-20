# 서로다른 n개의 자연수 합이s, n의 최대값?

s = int(input())
N = 0  # 갯수세기
result = 0  # 값 넘어가는지 체크하는 변수

for i in range(1, s):
    result += i
    N += 1
    if(result > s):
        N -= 1
        break
print(N)
