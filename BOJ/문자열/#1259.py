import sys
input = sys.stdin.readline

while True:
    case = input().rstrip()
    if case == "0":
        break
    if case == case[::-1]:
        print("yes")
    else:
        print("no")