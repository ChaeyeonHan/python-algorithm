import sys

N = int(sys.stdin.readline().rstrip())
nums=[]
cards=[]

for i in range(1, N+1):
    nums.append(i)  # 1, 2, 3.. ~N까지 삽입됨(N부터 넣어서 N이 제일 아래로)

# 맨 위에 있는거 버리고, 그다음에 맨 위에 있는 카드 맨 아래로 넣기
# => 큐가 맞는 것 같음
for _ in range(N-1):
    a = nums.pop(0)  # 맨 앞 버리고
    cards.append(a)
    temp = nums.pop(0)  # 그 다음수 맨뒤에 삽입하기
    nums.append(temp)

for i in cards:
    print(i, end=' ')
print(nums[0])