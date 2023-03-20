from collections import deque
def bfs(num,visited,computers):
    q = deque()
    q.append(num)
    visited[num] = 1

    while q:
        node = q.popleft()

        for idx, is_connect in enumerate(computers[node]):
            if is_connect and idx != node and not visited[idx]:
                q.append(idx)
                visited[idx] = 1
                    
def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(200)]
       
    for i in range(len(computers)):
        if not visited[i]:
            bfs(i,visited,computers)
            answer += 1
        
    return answer