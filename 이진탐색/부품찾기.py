# 내가 푼거
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if M_list[i] in N_list:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 1.이진탐색(반복문으로 구현)
n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

def binary_search(array, target, start, end):
    mid = (start+end)//2
    while start <= end:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 2.계수 정렬
n = int(input())
array = [0]*1000001  # 모든 원소의 번호를 포함할 수 있는 리스트 생성

for i in input().split():  # 부품 번호를 입력받아서 저장하기
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] != 1:  # 원소가 없는 경우
        print('no', end=' ')
    else:
        print('yes', end=' ')


# 3.집합 자료형 이용
# set이용 => 특정한 데이터가 존재하는지 검사할때 유용하게 사용됨

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
