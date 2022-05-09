import sys
T = int(sys.stdin.readline())

while T:
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    print(nums[-3])
    T -= 1