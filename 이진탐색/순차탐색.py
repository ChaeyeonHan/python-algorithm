# 탐색 범위가 2000만 넘는다 -> 이진탐색 시도해보기 : O(logN)
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print("생성할 원소 개수를 입력한 다음 한 칸을 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요, 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

# 재귀함수로 구현하는 순차탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:  # 중간 > 찾으려는 값
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

# 반복문으로 구현하는 순차탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)