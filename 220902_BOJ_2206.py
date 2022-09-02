# BOJ 2206번 벽 부수고 이동하기

from collections import deque

H,W = map(int,input().split())
mapp = [list(map(int,input())) for _ in range(H)]
visited = [[[0] * 2 for _ in range(W)] for _ in range(H)]

q = deque()
q.append((0,0,0))
# y,x,벽을 부순 횟수
visited[0][0][0] = 1

while q:
    y, x, k = q.popleft()
    for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= nx < W and 0 <= ny < H and visited[ny][nx][k] == 0:
            # 벽을 한 번 부쉈든, 안부쉈든, 길이면 q에 추가
            if mapp[ny][nx] == 0:
                visited[ny][nx][k] = visited[y][x][k] + 1
                q.append((ny,nx,k))
            # 벽을 한 번도 부수지 않았는데 벽이면 q에 추가, 부수고 간 값 추가
            if mapp[ny][nx] == 1 and k == 0:
                visited[ny][nx][1] = visited[y][x][k] + 1
                q.append((ny,nx,1))
# 최솟값 출력
result = 0
if visited[H-1][W-1][0] == 0 and visited[H-1][W-1][1] == 0:
    result = -1
else:
    if visited[H-1][W-1][0] == 0:
        result = visited[H-1][W-1][1]
    elif visited[H-1][W-1][1] == 0:
        result = visited[H - 1][W - 1][0]
    else:
        result = min(visited[H-1][W-1][0],visited[H-1][W-1][1])

if H-1 == 0 and W-1 == 0:
    result = 1

print(result)
