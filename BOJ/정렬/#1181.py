import sys
n = int(sys.stdin.readline())

words=[]
for _ in range(n):
    words.append(sys.stdin.readline().strip())
set_list = set(words)  # 중복제거를 해준다
# list = set(list) X -> set을 하면 {}로 나온다! 다시 리스트로 변환해줘야 한다.
words = list(set_list)

words.sort()
words.sort(key=len)

for i in words:
    print(i)