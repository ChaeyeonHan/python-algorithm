# 구해야하는 집합 A가 있으면 A의 여집합을 구하고, 여집합에 포함되지 않은 요소들을 찾는 방식
numbers = list(range(1, 10_001))  # 10001이랑 같음. 큰수의 구분을 쉽게 하기 위해 숫자 중간에 언더바 사용

remove_list = []  # 생성자 리스트

for num in numbers:
    for i in str(num):  # 각자리 분산을 위해 str으로
        num += int(i)
    if num <= 10000:
        remove_list.append(num)

for remove_list in set(remove_list):  # 중복된 숫자 제거
    numbers.remove(remove_list)
for i in numbers:
    print(i)


# 다른 풀이
def d(n):
    n += sum(map(int, str(n)))
    return n

not_selfnum = set()  # 셀프넘버가 아닌 수들(생성자가 있는 수)

for i in range(1, 10001):
    not_selfnum.add(d(i))

for i in range(1, 10001):
    if i not in not_selfnum:
        print(i)
