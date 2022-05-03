'''
특정한 조건이 부합할때만 사용가능하지만, 매우 빠른 정렬 알고리즘
=> 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을때만 사용가능하다.
=> 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 한다.
 계수정렬은 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복될수록 유리한 알고리즘이다. 
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5 , 2]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')