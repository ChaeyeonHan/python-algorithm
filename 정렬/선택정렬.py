'''
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정
=> 알고리즘 문제풀이에 사용하기에는 다소 느린편
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]   # 스와프해서 바꿔주기

print(array)