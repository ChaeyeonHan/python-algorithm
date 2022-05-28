import sys
people = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    people.append([a, b])


for i in people:
    rank=1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1  #순위가 하나 뒤로 밀린다(자기보다 몸무게,키가 큰 사람들 세주기)
    print(rank, end=' ')