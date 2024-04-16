import sys
input = sys.stdin.readline

str = list(map(str, input().split().rstrip()))
result = 0  # 잘린 갯수

# ( 이 들어오면 스택에 넣어준다
# ) 가 나오는 경우, 이전 문자가 (라면 쇠막대기가 잘리고, )라면 쇠막대기라는 뜻
stack = []
for i in range(len(str)):
    if str[i] == '(':
        stack.append(str[i])
    else:  # )
        if str[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)