from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(500001)]    # 경로 정보를 담는 그래프
    
    for src, des in roads:
        graph[src].append(des)
        graph[des].append(src)

    # 목적지에서 각 지역까지의 최단 경로를 구하는 BFS
    q = deque()
    q.append(destination)
    visited = [0 for _ in range(500001)]
    visited[destination] = 1

    while q:
        now = q.popleft()

        for nq in graph[now]:
            if not visited[nq]:
                q.append(nq)
                visited[nq] = visited[now] + 1
    
    # 결과값 출력
    for source in sources:
        answer.append(visited[source] - 1)
    
    return answer