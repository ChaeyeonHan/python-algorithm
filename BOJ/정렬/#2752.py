import sys
a, b, c = map(int, sys.stdin.readline().split())

if a > b:
    if c > a:  # c a b
        print(b, a, c)
    elif b > c:  # a b c
        print(c, b, a)
    else:  # a c b
        print(b, c, a)
else:  # a < b
    if c < a:  # b a c
        print(c, a, b)
    elif b < c:  # c b a
        print(a, b, c)
    else:
        print(a, c, b)