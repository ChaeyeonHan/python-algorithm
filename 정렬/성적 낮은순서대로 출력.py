N = int(input())
# (학생이름, 점수)의 형태로 리스트에 저장
array = []
for i in range(N):
    input_data = input().split()
    # 점수는 int로 바꿔서 저장
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda x: x[1])


# for x in array:
#     print(x[0], end=' ')
for i in array:
    print(i[0], end=' ')