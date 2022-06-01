nums = list(map(int, input().split()))
result=0
for i in nums:
    result += i*i
result = result % 10
print(result)