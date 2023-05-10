import sys
input = sys.stdin.readline

nums_list = list(map(int, input().split()))
nums_list.sort()
print(nums_list[1])