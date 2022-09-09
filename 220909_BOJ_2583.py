# BOJ 2583번 영역 구하기

from collections import deque
# BFS
def bfs(y,x):
    area = 0
    que = deque()
    que.append((y,x))
    visited[y][x] = 1
    while que:
        qy,qx = que.popleft()
        # pop할 때 마다 영역 크기 +1
        area += 1
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = qy+dy
            nx = qx+dx
            if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and mapp[ny][nx] == 0:
                que.append((ny,nx))
                visited[ny][nx] = 1
    # 최종 영역의 넓이 추가
    areas.append(area)

H,W,K = map(int,input().split())
mapp = [[0 for _ in range(W)] for _ in range(H)]
visited = [[0 for _ in range(W)] for _ in range(H)]
# 직사각형 1로 표시
for _ in range(K):
    sx,sy,ex,ey = map(int,input().split())
    for i in range(sy,ey):
        for j in range(sx,ex):
            mapp[i][j] = 1

result = 0
areas = []
for i in range(H):
    for j in range(W):
        if mapp[i][j] == 0 and not visited[i][j]:
            bfs(i,j)
            result += 1

areas.sort()
print(result)
print(*areas)
