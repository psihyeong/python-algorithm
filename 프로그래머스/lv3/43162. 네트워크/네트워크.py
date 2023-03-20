def solution(n, computers):
    def dfs(start, visited):
        visited[start] = True
        for i in range(n):
            if computers[start][i] and not visited[i]:
                dfs(i, visited)
        
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, visited)
            answer += 1
            
    return answer