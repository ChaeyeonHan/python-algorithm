# 내 풀이
n = int(input())
stores = list(map(int, input().split()))
stores.sort()  # 오름차순 정렬

m = int(input())
nums = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

answer=[]
for i in nums:
    result = binary_search(stores, i, 0, n-1)
    if result != None:
        answer.append('yes')
    else:
        answer.append('no')

for i in range(len(answer)):  # 출력
    print(answer[i], end=' ')


# 정답(+계수정렬)
n = int(input())
stores = [0] * 1000001

for i in input().split():
    stores[int(i)] = 1
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if stores[i] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 집합 자료형
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')