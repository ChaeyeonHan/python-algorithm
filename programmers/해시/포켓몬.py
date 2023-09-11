def solution(nums):
    answer = 0
    dict = {}
    for i in nums:
        dict[i] = dict.get(i, 0) + 1
    answer = min(len(nums)//2, len(dict))
    return answer