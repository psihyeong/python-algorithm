from collections import deque
 
def bfs(y,x,dis):
    q = deque()
    q.append((y,x))
    inhome = 0
    if homes[y][x]:
        inhome += 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] +1
                if visited[ny][nx] <= dis:
                    q.append((ny, nx))
                    if homes[ny][nx]:
                        inhome += 1
    return inhome
 
TC = int(input())
for tc in range(1, TC+1):
    N, fee = map(int,input().split())
    homes = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for r in range(1, N+2):
        oper = (r**2 + (r-1)**2)
        for i in range(N):
            for j in range(N):
                able_home = bfs(i,j,r)
                if able_home*fee - oper >= 0:
                    if result < able_home:
                        result = able_home
    print(f'#{tc} {result}')
