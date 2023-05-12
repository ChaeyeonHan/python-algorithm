import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_h = set()
for i in range(N):
    no_h.add(input().rstrip())

no_s = set()
for i in range(M):
    no_s.add(input().rstrip())

# 교집합 구하기
result = list(no_h & no_s)

# 처음에 명단을 set이 아니라 리스트로 받고,
# result = list(set(no_h) & set(no_s)) 로 해도 된다.

print(len(result))
result = sorted(result)

for i in result:
    print(i)