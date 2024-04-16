N = int(input())

people = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
    cnt = 0  # 왼쪽에 있는 키 큰 사람의 수
    for j in range(N):
        if cnt == people[i] and answer[j] == 0:  # 왼쪽에 있는 키 큰 사람수가 일치하고, 해당 자리에 아무도 없다면
            answer[j] = i+1
            break
        elif answer[j] == 0:
            cnt += 1
print(" ".join(map(str, answer)))