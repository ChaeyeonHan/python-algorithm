# 완전탐색 유형에 해당 (Brute Forcing)
# 완전탐색 문제는 비효율적인 시간 복잡도를 갖고 있으므로, 탐색해야할 데이터가 100만개 이하일때 사용하면 적적하다.

H = int(input())

count = 0
for i in range(H+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)