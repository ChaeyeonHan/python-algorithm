
def solution(N, number):
    answer = 0
    # 숫자 N을 사용해서 number 만들기(숫자는 최대 8번 사용가능하다)
    if N == number:
        return 1
    # 숫자 N 1개로 만들 수 있는 수들을 담은 집합, 숫자 N 2개로 만들 수 있는 수들을 담은 집합.. 8개까지
    s = [set() for _ in range(8)]
    # 각 set을 N * i의 갯수로 초기화
    # {N}, {NN}, {NNN} ..
    # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))

    for i in range(1, 8):
        for j in range(i):
            for x in s[j]:
                for y in s[i-j-1]:
                    s[i].add(x+y)
                    s[i].add(x-y)
                    s[i].add(x*y)

                    if y != 0:
                        s[i].add(x//y)
        if number in s[i]:
            answer = i+1  # N 사용횟수의 최솟값을 리턴
            break
    else:
        return -1

    return answer