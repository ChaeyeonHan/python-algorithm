def fibo_1(x):
    if x == 1 or x == 2:
        return 1
    return fibo_1(x-1) + fibo_1(x-2)

print(fibo_1(4))

# => 숫자가 커지면 수행 시간이 기하급수적으로 증가


# << 다이나믹 프로그래밍을 구현하는 방법 중 하나인 메모이제이션으로 풀어보기 >>
# 1. 탑다운 방식 : 큰문제를 해결하기 위하여 작은 문제를 호출
d = [0]*100   # 계산된 결과를 메모이제이션하기 위한 리스트 초기화

def fibo(x):
    # print('f(' + str(x) + ')', end=' ')  # 어떤함수 호출됬는지 출력하도록
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:  # 앞에서 계산을 했다면 계산결과를 그대로 반환
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


# 2. 보텀업 방식: 반복문을 이용하여 작은 문제부터 답을 도출
d = [0]*100
d[1] = 1
d[2] = 2
n=99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])