# 피보나치 수열
n = int(input())
result = 1
temp2 = 0
# n-2//n-1//n
for i in range(n-1):
    temp1 = result
    result = temp1 + temp2
    temp2 = temp1

print(result)

'''
# 리스트 이용
n = int(input())
array = [0, 1]
for i in range(2, n+1):
    array.append(array[-1] + array[-2])

print(array[n])
'''