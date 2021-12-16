'''
주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
단, 특정 숫자를 연속으로 K번을 초과해 사용할 수 없음

가장 큰 수와 두번째로 큰 수만 저장하면 된다.
'''

N, M, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort()  # 내장된 정렬 함수 사용
max_first = a[N-1]
max_second = a[N-2]

result = 0

while(1):
    for i in range(K):
        if M == 0:
            break
        result += max_first
        M -= 1  # 더할때마다 횟수 1씩 감소
    if M == 0:
        break
    result += max_second
    M -= 1

print(result)



