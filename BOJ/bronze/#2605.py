# insert()함수 사용!! -> insert(인덱스, 값)
N = int(input())

nums = list(map(int, input().split()))
result = []

for i in range(N):
    result.insert(i-nums[i], i+1)
# 예제 넣어보기 nums=[0,1,1,3,2]
# i=0, insert(0, 1) -> result=[1]
# i=1, insert(0, 2) -> result=[2,1]
# i=2, insert(1, 3) -> result=[2,3,1]
# i=3, insert(0, 4) -> result=[4,2,3,1]
# i=4, insert(2, 5) -> result=[4,2,5,3,1]

for i in result:
    print(i, end=' ')