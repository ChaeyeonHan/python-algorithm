import sys
N = int(input()) # 좌표 몇개인지
# N = int(sys.stdin.readline())
array=[] # 2차원 배열생성

for i in range(N):
    [a,b] = map(int,sys.stdin.readline().split())
    array.append([a,b])

array = sorted(array)
# 파이썬 내장함수인 sorted함수를 이용해서 오름차순 정렬

for i in range(N) :
    print(array[i][0], array[i][1])
