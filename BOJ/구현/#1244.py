import sys
input = sys.stdin.readline

N = int(input())
switches = [-1] + list(map(int, input().split()))  # 스위치 상태
nums = int(input())

def change(i):
    if switches[i]:
        switches[i] = 0
    else:
        switches[i] = 1
    return

for _ in range(nums):
    gender, number = map(int, input().split())  # 성별, 번호
    if gender == 1:  # 남학생
        for i in range(number, N+1, number):
            change(i)
    elif gender == 2:  # 여학생
        change(number)
        temp = 1  # 좌우로 넓힐 칸 수
        while 1 <= (number-temp) and (number+temp) <= N and switches[number-temp] == switches[number+temp]:  # 좌우 대칭이면
                change(number-temp)
                change(number+temp)
                temp += 1
    # print(switches)
for i in range(1, len(switches)):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()
