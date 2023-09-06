from itertools import permutations

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:  # 나누어 떨어진다면 소수X
            return False
    return True


def solution(numbers):
    nums = [i for i in numbers]
    per = []
    answer = []
    for i in range(1, len(nums)+1):
        per += list(permutations(nums, i))   # i개씩
    new_nums = [int("".join(k)) for k in per]
    for num in new_nums:
        if is_prime_number(num):  # 소수라면
            answer.append(num)
    return len(set(answer))
