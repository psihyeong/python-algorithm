# BOJ 1068번 트리

from collections import deque

N = int(input())        # 노드의 개수
p = list(map(int,input().split()))      # 0번 노드부터 N-1번 노드까지, 각 노드의 부모 리스트
del_n = int(input())        # 지울 노드의 번호
tree = [[] for _ in range(N)]
# 루트노드 찾기, 양방향 트리 만들기
for i in range(N):
    src, dest = p[i], i
    if src != -1:
        tree[src].append(dest)
        tree[dest].append(src)
    else:
        root = i

result = 0
# 노드의 방문 리스트
visited = [0 for _ in range(N)]     # 노드의 방문 리스트
# 지울 노드는 방문처리해서 방문하지 못하게 함
visited[del_n] = 1
# 리프 노드를 찾기 위한 BFS
q = deque()
# 루트 노드부터
q.append(root)
visited[root] = 1
while q:
    # 현재 노드
    now = q.popleft()
    is_leaf = True
    # 현재 노드와 연결된 노드 중에서
    for next in tree[now]:
        # 방문하지 않은 노드가 있으면
        if not visited[next]:
            visited[next] = 1
            q.append(next)
            # 리프노드는 아님
            is_leaf = False
    # 연결된 노드들 중에 방문하지 않은 노드가 없다면 리프노드
    if is_leaf:
        result += 1
        
# 자르는 노드가 루트노드면 결과값 0.
if del_n == root:
    result = 0

print(result)
