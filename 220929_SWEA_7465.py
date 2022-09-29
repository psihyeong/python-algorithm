# SWEA 7465번 창용 마을 무리의 개수

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):  # (부모테이블, 노드의 번호)
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
 
 
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
 
for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    parent = [0] * (N + 1)  # 부모 테이블 초기화하기
 
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, N + 1):
        parent[i] = i
 
    # Union 연산을 각각 수행
    for i in range(M):
        a,b = map(int,input().split())
        union_parent(parent, a, b)
        union_parent(parent, b, a)
 
    res = 0
    for i in range(1,N+1):
        if i == parent[i]:
            res += 1
    print(f'#{tc} {res}')
