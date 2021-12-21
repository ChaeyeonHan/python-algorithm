#numbers = list(map(int, input().split()))
numbers=[]
for i in range(9):
    numbers.append(int(input()))

cnt = 0
max = numbers[0]
for i in range(9):
    if (numbers[i] > max):
        max = numbers[i]
        cnt = i

print(max)
print(cnt+1)



# 두번째
num_list=[]
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)