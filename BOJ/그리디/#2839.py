'''
설탕이 5로 나눠지면 5키로로 나눠서 구하고,
나눠지지 않는다면 3씩 빼면서 남은 무게가 5로 나눠지는지 확인한다.
'''
sugar = int(input())
count = 0

while True:
    if(sugar % 5) == 0:
        count += sugar // 5
        print(count)
        break
    sugar -= 3  # 5로 나누어지지 않는 경우, 3씩 빼주면서 5의 배수인지 확인한다.
    count += 1
    if (sugar < 0):
        print(-1)
        break