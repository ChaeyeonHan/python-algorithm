data = input()
count0 = 0  #전부 0으로 바꾸는 경우
count1 = 0  #전부 1로 바꾸는 경우

# 첫번째 원소에 대해 먼저 바꿔주기
if data[0] == '1':
    count0 += 1  # 맨앞이 1일때 0으로 바꿔주기
else:
    count1 += 1  # 맨앞이 0일때 1로 바꿔주기

for i in range(len(data)-1):
    if data[i] != data[i+1]:  # 다를 때
        if data[i+1] == '1':  # 1인 경우
            count0 += 1
        else:   # 0인 경우
            count1 += 1

print(min(count0, count1))