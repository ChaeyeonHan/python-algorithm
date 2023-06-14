import sys
input = sys.stdin.readline

T = int(input())

while T != 0:
    N = int(input())
    people = []
    cnt = 1  # 서류 1등
    for _ in range(N):
        num1, num2 = map(int, input().split())
        people.append([num1, num2])
    people.sort(key=lambda x: x[0])  # 서류 순위로 정렬
    rank = people[0][1]

    for i in range(1, N):
        if rank > people[i][1]:
            cnt += 1
            rank = people[i][1]
    print(cnt)
    T -= 1