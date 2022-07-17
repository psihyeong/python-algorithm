from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    result = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx,ny))
                elif graph[nx][ny] == 3:
                    result = 1
                    break
                    
    return result
        
dx, dy = [-1,1,0,0], [0,0,-1,1] 

for _ in range(10):
    tc = int(input())
    graph=[]
    x,y = 0,0
    for i in range(16):
        graph.append(list(map(int,input())))  
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                x = i
                y = j

    print(f"#{tc} {bfs(x,y)}")