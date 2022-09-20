# BOJ 1600번 말이 되고픈 원숭이
from collections import deque

def bfs(y,x):
    q = deque()
    q.append((y,x,K))

    while q:
        y,x,z = q.popleft()
        # 결과값, 근데 이제 가장 빨리 도착한
        if y == H-1 and x == W-1:
            return visited[y][x][z]
        for dy,dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny = dy+y
            nx = dx+x
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][z]:
                if graph[ny][nx] != 1:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    q.append((ny,nx,z))
            # 말 이동 가능하면
            if z > 0:
                for dy, dx in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < H and 0 <= nx < W and graph[ny][nx] != 1:
                        # 해당 좌표에 말 이동을 쓰고 도착하지 않았다면
                        if not visited[ny][nx][z-1]:
                            # 사용해서 도착
                            visited[ny][nx][z-1] = visited[y][x][z] + 1
                            # 능력 1회 사용한 좌표 append
                            q.append((ny,nx,z-1))

    return -1

K = int(input())
W, H = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]
visited = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
print(bfs(0,0))
