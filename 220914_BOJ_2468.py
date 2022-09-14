# BOJ 2468번 안전 영역
from collections import deque

# 인접한 안전 영역들을 방문처리 해주는 BFS
def bfs(y,x,rain_height):
    que = deque()
    que.append((y,x))
    visited[y][x] = 1
    while que:
        qy,qx = que.popleft()
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = qy+dy
            nx = qx+dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and mapp[ny][nx] >= rain_height:
                que.append((ny,nx))
                visited[ny][nx] = 1


N = int(input())
mapp = [list(map(int,input().split())) for _ in range(N)]
# 비 높이에 따른 안전한 영역의 수
result = []
# 비 높이의 모든 경우의 수
for rain in range(1,101):
    area = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mapp[i][j] >= rain and not visited[i][j]:
                # 해당 영역 방문처리
                bfs(i,j,rain)
                # 영역 수 +1
                area += 1
    result.append(area)

print(max(result))
