import sys
input = sys.stdin.readline

array1 = list(input().rstrip())
array2 = []
n = int(input())

for _ in range(n):
    command = input().rstrip()
    if command[0] == 'L':
        if array1:
            array2.append(array1.pop())
            # print(array1, array2)
    elif command[0] == 'D':
        if array2:
            array1.append(array2.pop())
            # print(array1, array2)
    elif command[0] == 'B':
        if array1:
            array1.pop()
            # print(array1, array2)
    else:
        array1.append(command[-1])
        # print(array1, array2)

array1.extend(reversed(array2))
print("".join(array1))