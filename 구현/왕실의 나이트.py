'''
입력위치 행과 열이 모두 숫자가 아니라 문자와 함께 있는 경우
'''

position = input()   #a
row = int(position[1])  #1
#column = int(ord(position))-int(ord('a'))+1  position에 두개 다 들어가서 X
column = int(ord(position[0]))-int(ord('a'))+1

# 이동할 수 있는 8가지 방향, dx,dy를 대신하여 사용되는 방법
steps = [(1,2), (-1,2), (2,-1), (2,1), (-1,-2), (1,-2), (-2,-1), (-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if (next_row >=1 and next_row <= 8 and next_column >=1 and next_column <= 8 ):
        result += 1

print(result)