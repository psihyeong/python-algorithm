from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)       # 여행경로를 담는 인접리스트
    visited = defaultdict(list)     # 인접리스트 방문체크
    
    for src, dest in tickets:
        graph[src].append(dest)
        visited[src].append(0)
    
    for key, value in graph.items():
        graph[key].sort()           # 알파벳순 정렬
    
    
    def dfs(ticket, path):
        if len(path) == len(tickets):
            answer.append(path)
            return
                 
        for idx in range(len(graph[ticket])):
            if not visited[ticket][idx]:
                visited[ticket][idx] = 1
                dfs(graph[ticket][idx],path+[graph[ticket][idx]])
                visited[ticket][idx] = 0
                
    dfs("ICN", [])
    answer.sort()
    
    return ["ICN"] + answer[0]