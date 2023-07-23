import sys
input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

result = []
def cut(x, y, N):
    num = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != paper[i][j]:
                N = N//3
                cut(x, y, N)
                cut(x+N, y, N)
                cut(x+2*N, y, N)
                cut(x, y+N, N)
                cut(x, y+2*N, N)
                cut(x+N, y+N, N)
                cut(x+2*N, y+N, N)
                cut(x+N, y+2*N, N)
                cut(x+2*N, y+2*N, N)
                return
    if num == 0:
        result.append(0)
    elif num == -1:
        result.append(-1)
    else:
        result.append(1)
cut(0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))