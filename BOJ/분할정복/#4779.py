import sys
input = sys.stdin.readline

def cantor(array, start, N):  # start : 시작점
    if N == 1:
        return
    for i in range(start + N // 3, start + N // 3 * 2):  # 가운데 문자열 공백으로 만들기
        array[i] = ' '
    cantor(array, start, N // 3)
    cantor(array, start + N // 3 * 2, N // 3)


while True:
    try:
        N = int(input())
        result = ['-'] * (3 ** N)
        # result = ['-' for _ in range(pow(3, N))]
        cantor(result, 0, 3 ** N)
        print("".join(result))
    except:
        break
