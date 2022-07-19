from collections import deque
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q,end=' ')
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N,M,v = map(int,input().split())
graph = [[]*(N+1) for _ in range(N+1)] # 그래프 그리기


for _ in range(M):  #노드 설정
    m1, m2 = map(int,input().split())
    graph[m1].append(m2)
    graph[m2].append(m1)

for i in graph:
    i.sort()

visited = [False]*(N+1)
dfs(graph,v,visited)
print()
visited = [False]*(N+1) #방문기록 초기화
bfs(graph,v,visited)