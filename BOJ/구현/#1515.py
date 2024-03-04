import sys
input = sys.stdin.readline

nums = input().rstrip()
i = 0
while True:
    i += 1  # 1부터 증가하는 자연수
    num = str(i)
    while len(nums) > 0 and len(num) > 0:
        if num[0] == nums[0]:  # 일치하면 숫자 잘라내기
            nums = nums[1:]
        num = num[1:]  # 앞자리 제거(숫자가 두자리 이상)
    if nums == '':
        print(i)
        break