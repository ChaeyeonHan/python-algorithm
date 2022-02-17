import sys
def merge(a, b):  # 팀 합치기
    a = find_parent(parent, a)
    b= find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a):  # 같은 팀 여부 확인 => 즉, 부모찾기
    if parent[a] != a:  # 루트노드(부모노드)가 아니라면, 찾을 때까지 재귀적으로 호출
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (n+1)  # 초기화

for i in range(n+1):  # 초기에는 각자 모두 다른 팀(부모)으로 구분됨
    parent[i] = i

for i in range(m+1):
    op, a, b = map(int, sys.stdin.readline().rstrip().split())  # 입력받기
    if op == 0:  # 0ab : 합치기
        merge(a, b)
    elif op == 1:  # 1ab: 같은 팀 여부 확인
        if find_parent(parent,a) == find_parent(parent, b):  # 같은 팀에 속해있다면(루트 노드가 동일한 경우)
            print("YES")
        else:
            print("NO")
