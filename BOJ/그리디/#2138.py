import sys
input = sys.stdin.readline

N = int(input())
status = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))


def change(A, B):
    temp = A[:]
    press = 0
    for i in range(1, N):
        if temp[i - 1] == B[i - 1]:  # 현재 스위치 상태가 target 값과 같은지 비교
            continue
        press += 1
        for j in range(i - 1, i + 2):
            if j < N:  # 값이 다르면, i-1, i, i+1 위치 반전(마지막 스위치는 i+1번째가 없음!)
                temp[j] = 1 - temp[j]
    if temp == B:
        return press
    else:  # 만들 수 없는 경우
        return 1e9


result = change(status, target)

# 첫번째 전구를 누르는 경우
status[0] = 1-status[0]
status[1] = 1-status[1]

answer = min(result, change(status, target) + 1)  # (첫번째를 누르지 않는경우, 누르는 경우)

if answer != 1e9:
    print(answer)
else:
    print(-1)
