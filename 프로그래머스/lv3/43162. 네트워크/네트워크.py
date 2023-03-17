from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(200)]
    
    def bfs(num):
        q = deque()
        q.append(num)
        visited[num] = 1
        
        while q:
            node = q.popleft()
            
            for idx, is_connect in enumerate(computers[node]):
                if is_connect and idx != node and not visited[idx]:
                    q.append(idx)
                    visited[idx] = 1
            
    for i in range(len(computers)):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer