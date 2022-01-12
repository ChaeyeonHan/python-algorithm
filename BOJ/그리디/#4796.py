days = 0
count = 1

while True:
    L, P, V = map(int, input().split())
    if (L == 0 and P == 0 and V == 0):  # 모두 0이 들어오기 전까지 반복
        break
    s1 = (V // P) * L
    # s2 = min((V%P), L)
    s2 = L if V % P > L else V % P  # 삼항연산자 사용

    print('Case %d: %d' %(count, s1+s2))
    count += 1