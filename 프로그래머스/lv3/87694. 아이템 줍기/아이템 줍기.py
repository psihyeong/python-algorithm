from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    for rec in rectangle:
        ldx, ldy, rux, ruy = map(lambda x:x*2, rec)     # 좌표를 2배로 늘려줘야 1차이의 지점이 연결되지 않음
        for x in range(ldx,rux+1):
            for y in range(ldy,ruy+1):
                if ldy < y < ruy and ldx < x < rux:     # 사각형 내부는 0
                    graph[y][x] = 0 
                elif graph[y][x] != 0:                  # 테두리면서, 다른 사각형의 내부가 아니면 테두리 1
                    graph[y][x] = 1
    
    # BFS
    visited = [[1 for _ in range(102)] for _ in range(102)]
    
    q = deque()
    q.append((characterY*2,characterX*2))
    visited[characterY*2][characterX] = 1
    
    while q:
        y,x = q.popleft()
        if y == itemY*2 and x == itemX*2:
            answer = visited[y][x] // 2
            break
            
        for dy,dx in [(-1,0),(0,1),(0,-1),(1,0)]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < 102 and 0 <= nx < 102 and graph[ny][nx] == 1 and visited[ny][nx] == 1:
                q.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1
                
    
        
    
    return answer