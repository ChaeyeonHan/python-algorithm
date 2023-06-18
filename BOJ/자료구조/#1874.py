import sys
input = sys.stdin.readline
stack = []
operator = []
flag = True

N = int(input())
start = 1

for i in range(N):
    num = int(input())
    while start <= num:  # 스택에 숫자 push
        operator.append("+")
        stack.append(start)
        start += 1

    if stack[-1] == num:  # 스택에서 꺼내기(pop)
        stack.pop()
        operator.append("-")
    else:
        print("NO")
        flag = False
        break

if flag:
    for i in operator:
        print(i)