import sys
input = sys.stdin.readline

N = input().rstrip()
# N = int(input())
# int로 입력받으면 iterable(값을 꺼낼 수 있는 객체)하지 않아서 for문 돌릴수가X => 그래서 문자열로 입력해준다다
# iterable한 객체 : list, dict, set, str, tuple, range
result = []
for i in N:  # 각 숫자를 자릿수를 나눠서 배열에 저장
    result.append(int(i))

result.sort(reverse=True)
for i in result:
    print(i, end='')