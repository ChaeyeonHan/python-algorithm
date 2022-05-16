N = list(input())   # 210입력
sum = 0
for i in N:
    sum += int(i)
# print(sum)
N.sort(reverse=True)

# 30의 배수 -> 각자리들의 합이 3의 배수, 일의 자리가 0
if (sum % 3 != 0) or ("0" not in N):
    print(-1)
else:
    print("".join(N))