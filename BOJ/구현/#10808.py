S = input()
count = [0]*26

for i in S:
    pos = ord(i) - 97
    count[pos] += 1

for i in count:
    print(i, end=' ')
