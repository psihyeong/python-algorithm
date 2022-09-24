# BOJ 11725번 트리의 부모 찾기

def dfs(root):
    stack = [root]
    while stack:
        tmp = stack.pop()
        for i in tree[tmp]:
            # 부모리스트에 i의 부모로 tmp를 넣어주고
            parent[i].append(tmp)
            stack.append(i)
            # 트리에서 i의 자식 tmp를 제거
            tree[i].remove(tmp)
            print(tree)
            print(parent)

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]

for _ in range(N-1):
    jun, hu = map(int,input().split())
    tree[jun].append(hu)
    tree[hu].append(jun)

dfs(1)

for r in range(2,N+1):
    print(parent[r][0])
