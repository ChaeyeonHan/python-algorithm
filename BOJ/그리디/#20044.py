# 코딩 역량 합의 최솟값이 최대가 되게끔

N = int(input())
scores = list(map(int, input().split()))

scores.sort()
cnt = []

for i in range(len(scores)):
    cnt.append(scores[i] + scores[len(scores)-i-1])
print(min(cnt))
