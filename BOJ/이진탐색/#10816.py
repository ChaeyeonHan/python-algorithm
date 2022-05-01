# 딕셔너리 이용
# 숫자를 dict의 key로, 카드 숫자를 value로 해서 사전을 만든다
n = int(input())
cards = list(map(int, input().split()))
cards.sort()  # 상근이 카드

m = int(input())
targets = list(map(int, input().split()))

# 딕셔너리에 담아주기
dic = dict()
for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in targets:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')