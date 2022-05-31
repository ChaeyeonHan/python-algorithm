import sys

n, k = map(int, sys.stdin.readline().split())
medals=[]
for _ in range(n):
    medals.append(list(map(int, sys.stdin.readline().rstrip().split())))

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)  # 금,은,동 많은 순서대로 넣어준다
# medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if medals[i][0] == k:
        index = i  # 해당 국가의 index찾아주기
for i in range(n):  # 등수가 같은 나라가 있을 경우를 위해 (그 국가의 index + 1)의 등수
    if medals[index][1:] == medals[i][1:]:
        print(i+1)
        break

# # 2차원 배열
n, k = map(int, sys.stdin.readline().split())

medals=[[] for _ in range(n+1)]  # 여기 n아님!!
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    medals[a] = [b, c, d]
    # medals[a].append([b, c, d])  # 금, 은, 동 순으로 넣어준다  # 이건 왜 안되는걸까...?
gold, silver, bronze = medals[k]
# print(gold, silver, bronze)

rank=1
for i in range(1, n+1):
    if medals[i][0] > gold:  # 금 더 많다
        rank += 1
    elif medals[i][0] == gold:  # 금 갯수 동일
        if medals[i][1] > silver:  # 은 더 많다
            rank += 1
        elif medals[i][1] == silver:  # 은 갯수 동일
            if medals[i][2] > bronze:  # 동 갯수 많다
                rank += 1
print(rank)
