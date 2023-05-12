import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 나무의 수, 가져가려는 나무 길이
heights = list(map(int, input().split()))
heights.sort()

def find_height(array, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2  # 절단기 길이
        for i in array:
            if i > mid:  # 나무가 절단기보다 더 긴 경우
                total += (i-mid)
        if total < M:  # 나무가 부족 -> 절단기 길이를 더 줄여야 한다 -> 왼쪽으로 이동
            end = mid - 1
        else:  # 나무가 많이 잘렸기에 절단기 더 높인다 -> 오른쪽 이동
            start = mid + 1
            result = mid
    return result

print(find_height(heights, 0, max(heights)))