S = input()

# 첫번째 문자를 숫자로바꿔 넣는다
result = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)