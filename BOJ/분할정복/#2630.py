import sys
input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
result = []

def cut(x, y, N):
    color = paper[x][y]  # 처음 맨앞 색상
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                cut(x, y, N//2)
                cut(x, y+N//2, N//2)
                cut(x+N//2, y, N//2)
                cut(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    if color == 1:
        result.append(1)

cut(0, 0, N)
print(result.count(0))
print(result.count(1))