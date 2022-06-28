T = int(input())

while T:
    floor = int(input())  # 층과 호수를 입력
    num = int(input())
    f0 = [x for x in range(1, num+1)]  # 0층 인원수(1호~num호까지)

    for i in range(floor):
        for j in range(1, num): # 배열이 1호부터 시작하니까 num+1이 아니고 num.
            f0[j] = f0[j] + f0[j-1]

    print(f0[num-1])
    T -= 1