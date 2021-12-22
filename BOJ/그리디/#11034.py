# 문제에서 몇개의 테스트케이스인지 명시되어있지 않다.
# -> try, except이용해서

a, b, c = map(int, input().split())
cnt = 0
# max함수 사용하면 한줄에 쓸 수 있다
print(max(b-a, c-b)-1)
while True:
    try:
        a, b, c = map(int, input().split())
        print(max(b-a, c-b)-1)
    except:
        break
