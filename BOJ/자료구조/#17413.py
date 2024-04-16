import sys
input = sys.stdin.readline

str = input().rstrip() + ' '

stack = []
result = ''
flag = 0
for i in range(len(str)):
    if str[i] == '<':
        flag = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)
    if str[i] == '>':
        flag = 0
        for _ in range(len(stack)):
            result += stack.pop(0)
    if str[i] == ' ' and flag == 0:  # 공백&괄호 밖인 경우
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '  # 다시 공백 넣어주기

print(result)