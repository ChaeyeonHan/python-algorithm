import sys
T = int(sys.stdin.readline())

while T != 0:  # 0이되면 테스트 종료
    N = int(sys.stdin.readline())
    people = []
    cnt = 1  # 합격자 카운트! 서류 1위는 무조건 붙음
    for _ in range(N):
        num1, num2 = map(int, sys.stdin.readline().split())
        people.append([num1, num2])
    people.sort(key=lambda x: x[0])  #일단 서류 순위로 정렬
    rank = people[0][1]  # 서류 1위인 사람의 면접 순위를 넣어준다
    
    for i in range(1, N):
        if rank > people[i][1]:
            cnt += 1
            rank = people[i][1]
    print(cnt)
    T -= 1