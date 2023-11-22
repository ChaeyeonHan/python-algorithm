T = int(input())

for i in range(T):
    N, M, K = map(int, input().split())  # 사람수, M초의 시간 동안 K개의 붕어빵 생산
    arrive = list(map(int, input().split()))  # 도착시간
    arrive.sort()  # 오름차순 정렬

    for t in range(N):
        total = (arrive[t] // M) * K
        if total-(t+1) < 0:
            print(f'#{i+1}' + " Impossible")
            break
    else:
        print(f'#{i+1}' + " Possible")