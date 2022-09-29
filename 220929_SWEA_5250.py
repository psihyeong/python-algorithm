# SWEA 5250번 최소 비용

from collections import deque
 
def bfs():
    q = deque()
    q.append((0,0))
    while q:
        y,x = q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                tmp = graph[ny][nx] - graph[y][x]
                if tmp > 0:
                    if visited[y][x] + 1 + tmp < visited[ny][nx]:
                        visited[ny][nx] = visited[y][x] + 1 + tmp
                        q.append((ny,nx))
                else:
                    if visited[y][x] + 1 < visited[ny][nx]:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny,nx))
 
for tc in range(1,int(input())+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    result = int(1e9)
    visited = [[int(1e9) for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    bfs()
 
    print(f'#{tc} {visited[N-1][N-1]}')
