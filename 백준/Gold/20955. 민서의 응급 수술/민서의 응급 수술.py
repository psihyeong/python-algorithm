# BOJ 20955번 민서의 응급 수술
# 트리, 그래프

from collections import deque
import sys
input = sys.stdin.readline

# 트리를 싸이클없이 연결, 연결된 뉴런들을 방문처리하고, 사용한 시냅스 수를 더해주는 함수
def bfs(start):
    global used_syn
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for next in tree[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                used_syn += 1

N, M = map(int,input().split())     # 뉴런의 개수, 시냅스의 개수
tree = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())     # 시냅스로 연결된 두 뉴런의 번호
    tree[u].append(v)
    tree[v].append(u)

visited = [0 for _ in range(N+1)]
used_syn = 0
trees = 0
for i in range(1,N+1):
    # 방문처리 되지 않은 노드는
    if not visited[i]:
        # bfs를 통해 연결된 노드들의 집합들을 방문처리
        bfs(i)
        trees += 1

solo = 0
# 혼자남은 노드들의 개수
for i in range(1,N+1):
    if not visited[i]:
        solo += 1

# 총 트리의 개수 + 단독 노드의 개수 - 1은 연결하는 연산 수
connect = trees + solo - 1
# 총 시냅스에서, 사용한 시냅스 수를 빼면 연결을 끊는 연산 수
cut = M - used_syn
print(connect + cut)
