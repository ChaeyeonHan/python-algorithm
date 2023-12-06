import sys
input = sys.stdin.readline

A, B = map(int, input().split())  # A에서 B 만들기
answer = 1
while True:
    if A == B:
        break
    elif (B % 2 != 0) and (B % 10 != 1) or (B < A):
        answer = -1
        break
    else:
        if B % 10 == 1:
            B //= 10
            answer += 1
        elif B % 2 == 0:
            B //= 2
            answer += 1

print(answer)