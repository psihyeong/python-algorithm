# BOJ 2589번 보물섬

from collections import deque

# y,x에서 갈 수 있는 인접한 육지들의 최단거리를 갱신해주는 BFS
def bfs(y,x):
    global result
    q = deque()
    q.append((y,x))
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    visited[y][x] = 0
    while q:
        y,x = q.popleft()
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == -1 and graph[ny][nx] == 'L':
                q.append((ny,nx))
                dist = visited[y][x] + 1
                visited[ny][nx] = dist
                # dist가 최대일 때 보물이 묻혀있는 최단 거리이다.
                if dist > result:
                    result = dist

H,W = map(int,input().split())
graph = [list(map(str,input())) for _ in range(H)]
result = 0
# 모든 육지에서부터
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'L':
            # 출발
            bfs(i,j)
print(result)
