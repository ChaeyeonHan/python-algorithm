import sys
from collections import deque  # 스택과 큐의 기능을 모두 가진 객체. 출입구 양쪽에 모두 있음

n, k = map(int, sys.stdin.readline().rstrip().split())
q = deque()
result=[]

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())  # k번째마다 제거되어 result 배열에 추가된다
print('<', end='')
print(', '.join(map(str, result)), end='')  # join -> 매개변수로 들어온 리스트에 있는 요소를 합쳐 하나의 문자열로 바꾸어 반환하는 함수
print('>')