import sys
input = sys.stdin.readline

S = list(input().rstrip())
bomb = list(input().rstrip())

# while bomb in S:
#     S = S.replace(bomb, "")
#
# if S != "":
#     print(S)
# else:
#     print("FRULA")

stack = []
for i in range(len(S)):
    stack.append(S[i])
    # 맨 뒤 값부터 폭발 문자열 갯수만큼 가져와서 폭발 문자열과 같은지 비교
    if stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")