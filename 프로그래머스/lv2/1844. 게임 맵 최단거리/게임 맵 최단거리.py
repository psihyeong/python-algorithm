from collections import deque

def solution(maps):
    answer = 0
    
    width = len(maps[0])        # 진영 총 열
    height = len(maps)          # 진영 총 행
    
    visited = [[-1 for _ in range(width)] for _ in range(height)]   # 좌표에 도달할 수 있는 최솟값을 담는 배열
    
    # bfs
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        y,x = q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny = y + dy
            nx = x + dx
            
            if 0 <= ny < height and 0 <= nx < width and maps[ny][nx]:
                # 가장 빠른 길을 구하는 조건
                if visited[ny][nx] == -1 or visited[ny][nx] > visited[y][x] + 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))
    
    answer = visited[height-1][width-1]
    
    return answer