numbers=[]
count = 0

for i in range(10):
    n = int(input())
    numbers.append(n % 42)

# set함수 : 중복되지 않은 원소를 얻고자 할때 사용하는 파이썬 내장함수
s = set(numbers)
print(len(s))