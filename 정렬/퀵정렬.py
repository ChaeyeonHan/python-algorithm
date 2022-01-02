''' (피벗사용하는 알고리즘)
정렬알고리즘 중 가장 많이 사용되는 알고리즘이다.
퀵 정렬은 기준 데이터(pivot)을 설정한 다음 큰수와 작은수를 교환한후 리스트를 반으로 나누는 방식으로 동작한다.
피벗을 설정하고 왼쪽에서는 피벗보다 큰 값을 찾고, 오른쪽에서는 피벗보다 작은 값을 찾는다.  (재귀함수로 구현하면 간단해진다)

피벗과 다른 데이터를 계속 비교해야하므로, 비교연산 횟수가 증가하여 비효율적이지만, 직관적이고 기억하기 쉽다.
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 한개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:  # 피벗보다 큰 데이터를 찾을때까지 반복한다
            left += 1
        while right > start and array[right] >= array[pivot]:  # 피벗보다 작은 데이터를 찾을때까지 반복한다
            right -= 1
        if left > right:  # 엇갈린 경우, 작은데이터와 피벗 교환
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않은 경우, 큰데이터와 작은 데이터를 교환
            array[right], array[left] = array[left], array[right]
    # 분할이후 왼쪽, 오른쪽에서 각각 정렬을 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)