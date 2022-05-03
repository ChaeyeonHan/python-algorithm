'''
데이터를 하나씩 확인하여 정렬된 데이터들에서 적절한 위치에 삽입하는 방법이다
맨 앞의 데이터는 정렬되어있다고 가정하고 두번째 데이터부터 시작한다.
=> 데이터가 거의 정렬이 되어있는 경우에 매우 강력한 방법이다. 
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 맨앞은 제외하고 두번째부터 시작한다
    for j in range(i, 0, -1):  # i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j-1]:  # j의 데이터가 왼쪽의 데이터보다 작은경우
            array[j], array[j-1] = array[j-1], array[j]  # 위치바꿔준다
        else:
            break

print(array)