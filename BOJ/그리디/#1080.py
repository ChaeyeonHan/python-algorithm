N, M = map(int, input().split())
graph1 = []
graph2 = []
count = 0

def convertgraph(i, j):  # 3x3의 행렬을 뒤집는 함수
    for x in range(i, i+3):
        for y in range(j, j+3):
            graph1[x][y] = 1 - graph1[x][y]  # 0과 1을 뒤집는 연산이므로 1에서 값을 빼주고 update시켜준다.

# 행렬 입력 부분
for i in range(N):   # A함수 입력
    graph1.append(list(map(int, input())))
for i in range(N):   # B함수 입력
    graph2.append(list(map(int, input())))

for i in range(N-2):
    for j in range(M-2):
        if graph1[i][j] != graph2[i][j]:
            convertgraph(i, j)
            count += 1

flag = 0  # 변환할 수 있는지 나타내기 위한 변수

for i in range(N):
    for j in range(M):
        if graph1[i][j] != graph2[i][j]:
            flag = 1
            break
if flag == 1:
    print(-1)
else:
    print(count)