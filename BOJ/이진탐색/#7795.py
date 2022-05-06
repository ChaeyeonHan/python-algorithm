import sys
T = int(sys.stdin.readline().rstrip())

# mid는 인덱스 번호이고, res는 갯수!!
def binary_search(arr, value):
    start, end = 0, len(arr)-1
    res = -1
    while start <= end:
        mid = (start+end)//2
        if value > arr[mid]:  # A가 B의 값보다 큰 경우 -> 카운트해주기
            res = mid
            # print("res=mid값 : " + str(res))
            start = mid + 1
        else:
            end = mid - 1
    return res

while T:
    N, M = map(int, sys.stdin.readline().rstrip().split())
    nums_A = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    nums_B = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    cnt = 0
    for i in nums_A:
        cnt += (binary_search(nums_B, i)) + 1 # B리스트에서 i보다 작은거 찾기
    print(cnt)
    T -= 1

# 이렇게 원소 한개씩 비교하면 시간초과.
# while T:
#     N, M = map(int, sys.stdin.readline().rstrip().split())
#     nums_A = list(map(int, sys.stdin.readline().rstrip().split()))
#     nums_B = list(map(int, sys.stdin.readline().rstrip().split()))
#     cnt = 0
#     for i in nums_A:
#         for j in nums_B:
#             if i > j:
#                 cnt += 1
#     print(cnt)
#     T -= 1