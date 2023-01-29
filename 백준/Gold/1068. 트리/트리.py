# BOJ 1068번 트리
from collections import deque

N = int(input())        # 노드의 개수
p = list(map(int,input().split()))      # 0번 노드부터 N-1번 노드까지, 각 노드의 부모 리스트
del_n = int(input())        # 지울 노드의 번호

tree = [[] for _ in range(N)]

for i in range(N):
    src, dest = p[i], i
    if src != -1:
        tree[src].append(dest)
        tree[dest].append(src)
    else:
        root = i

result = 0

visited = [0 for _ in range(N)]
visited[del_n] = 1
q = deque()
q.append(root)
visited[root] = 1
while q:
    now = q.popleft()
    tmp = 0
    for next in tree[now]:
        if not visited[next]:
            visited[next] = 1
            q.append(next)
            tmp = 1
    if tmp == 0:
        result += 1

if del_n == root:
    result = 0

print(result)