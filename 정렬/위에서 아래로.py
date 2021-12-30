N = int(input())
result=[]
for i in range(N):
    result.append(int(input()))
# 둘다 돌아감
# result = sorted(result, reverse=True)
result.sort(reverse=True)
for i in result:
    print(i, end=' ')