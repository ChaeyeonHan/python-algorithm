import sys
input = sys.stdin.readline

N = int(input())
nums = [input().rstrip() for _ in range(N)]

# 문자열 사전순으로 정렬 & 인덱스와 함께 저장.
# (인덱스, 문자열)
sorted_nums = sorted(list(enumerate(nums)), key=lambda x: x[1])  # 문자열 기준 정렬

def prefix_length(a, b):
    cnt = 0
    for idx in range(min(len(a), len(b))):
        if a[idx] == b[idx]:
            cnt += 1
        else:
            break
    return cnt

max_length = 0
length = [0] * (N+1)  # 최장 접두사 담을 리스트
for i in range(N-1):
    # 두 문자열의 접두사 길이 찾기
    cur = prefix_length(sorted_nums[i][1], sorted_nums[i+1][1])
    max_length = max(cur, max_length)
    length[sorted_nums[i][0]] = max(length[sorted_nums[i][0]], cur)
    length[sorted_nums[i+1][0]] = max(length[sorted_nums[i+1][0]], cur)
    
flag = 0
for i in range(N):
    if flag == 0:
        if length[i] == max(length):
            print(nums[i])
            prefix = nums[i][:max(length)]
            flag = 1
    else:
        if length[i] == max(length) and nums[i][:max(length)] == prefix:
            print(nums[i])
            break
            