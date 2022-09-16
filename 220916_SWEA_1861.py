# SWEA 1861번 정사각형 방

from collections import deque
import heapq
 
def bfs(y,x):
    q = deque()
    q.append((y,x))
    result = 1
    iy, ix = y, x
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1,0),(0,-1),(1,0),(0,1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if graph[y][x]+1 == graph[ny][nx]:
                    q.append((ny,nx))
                    visited[ny][nx] = True
                    result += 1
                elif graph[y][x] - 1 == graph[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    result += 1
                    iy,ix = ny, nx
    return result, graph[iy][ix]
 
TC = int(input())
 
for tc in range(1,TC+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            val, num = bfs(i,j)
            heapq.heappush(result,(-val,num))
 
    print(f'#{tc} {result[0][1]} {-result[0][0]}')
