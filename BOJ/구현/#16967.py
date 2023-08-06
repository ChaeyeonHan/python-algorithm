import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
B_array = [0 * (W+Y) for _ in range(H+X)]

for i in range(H+X):
    B_array[i] = list(map(int, input().split()))

A_array = [[0]* W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A_array[i][j] = B_array[i][j]

for i in range(X, H):
    for j in range(Y, W):
        A_array[i][j] = B_array[i][j] - A_array[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(A_array[i][j], end=' ')
    print("")