# << 파이썬 기초 >>
#  람다표현식 예시
def add(a,b) :
    return a+b
print((lambda a, b: a+b)(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
def my_key(x): # 두번째 값을 리턴시켜서 정렬기준을 명시
    return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key=lambda x: x[1]))

# 리스트 순서에 맞는 각 원소끼리 더하기
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)

print(list(result))


'''
<<사용빈도가 높은 표준 라이브러리>>
내장함수 : 기본입출력부터 정렬함수까지 기본적인 함수들을 제공(import없이 사용 가능하다)
itertools : 반복되는 형태의 데이터를 처리하기 위한 기능들을 제공, 특히 순열과 조합 라이브러리가 포함되어 있음(완전탐색유형에서)
heapq : 힙자료구조를 제공한다. 일반적으로 우선순위 큐 기능을 구현하기 위해 사용된다. (다익스트라와 같은 최단경로 알고리즘에서)
bisect : 이진탐색 기능을 제공한다.  
collections : 덱, 카운터등의 자료구조를 포함한다.
math : 필수적인 수학 기능을 제공
'''

##  1. 내장함수  ##

# sum() : 원소들의 합을 반환
result = sum([1,2,3,4,5])
print(result)

# min(), max() : 최소, 최대를 반환
min_value = min(7,5,3,1)
max_value = max(7,5,3,1)

# eval() : 수식을 계산해서 수로 반환
result = eval("(3+5)*7")
print(result)

# sorted() : 각 원소를 정렬한 값을 반환
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result, reverse_result)

# sorted() with key : key로 정렬기준을 알려준다
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

## 2. itertools -> 순열과 조합
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
from itertools import combinations
data = ['A', 'B', 'C']

result = list(combinations(data,2))
print(result)  # 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복순열
from itertools import product
data = ['A', 'B', 'C']

result = list(product(data, repeat=2)) # 2개를 뽑는 순열 구하기. 중복허용
print(result) # 결과 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
# 중복조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data,2))
print(result)

# Counter : 등장 횟수를 세는 기능을 제공한다.
# 리스트와 같은 반복가능한(iterable) 객체가 주어졌을때 내부의 원소가 몇번 등장했는지를 알려준다.
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['red'])
print(counter['green'])
print(dict(counter))  # 결과 : {'red': 2, 'blue': 3, 'green': 1} , 사전 자료형으로 반환

# math 라이브러리 : 수학적 기능을 제공한다
# 최대공약수를 구할때 math라이브러리의 gcd()함수를 이용할 수 있다.
import math

def lcm(a, b) :
    return a*b // math.gcd(a,b)

a = 21
b = 14

print(math.gc(21,14))  # 7
print(lcm(21,14))  # 42
