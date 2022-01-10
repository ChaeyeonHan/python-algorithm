N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0  # 감독관 수 카운트할 변수

for i in A:  # 모든 시험장의 응시자수에 대해서
    while A[i] != 0:  # 응시자수가 0이 될때까지
        if A[i] <= B:  # 총감독관만 있어도 되는 경우
            count += 1
            break
        else:  # 부감독관 필요한 경우
            count += 1
            A[i] -= A[i] - B
            A[i] += (A[i] // C)
            count += A[i] // C
            if A[i] % C == 0:  # 응시자수가 부감독관이 가능한 수로 나누어 떨어질때
                break
            else:  # 나누어 떨어지지 않으면 1을 더해준다
                count += 1
                break
print(count)


# 좀 더 줄여서 작성한 코드
for num in A:
    num -= B  # 총감독관 응시자수 빼주고
    count += 1
    if num > 0:
        if (num % C) == 0:  # 남은 응시자수에서 부감독관의 수 나눈값이 0이라면
            count += (num // C)
        else:  # 나머지 응시자들로 +1해주기
            count += (num // C) + 1


