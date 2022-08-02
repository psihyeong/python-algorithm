# BOJ 1325번 효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

# 기본 노드탐색 bfs
def bfs(graph, v, visited):
    temp = deque()
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        # q는 해킹한 컴퓨터 번호
        temp.append(q)
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return temp

N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
# b를 해킹하면 a를 해킹할 수 있다, b가 부모노드 a가 자식노드로 연결된 그래프
for i in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)

# result는 모든 컴퓨터 번호마다 bfs를 돌려서 해킹할 수 있는 수의 리스트
result = []
for i in range(1, N+1):
    visited = [0 for i in range(N+1)]
    if len(graph[i]) != 0 :
        result.append(len(bfs(graph, i, visited)))
    # 번호 수 맞추기 위해 연결된 게 없는 컴퓨터는 0을 채워줌
    else:
        result.append(0)

# 출력    
r = []
for i in range(len(result)):
    if result[i] == max(result):
        r.append(str(i+1))
        
print(' '.join(r))
