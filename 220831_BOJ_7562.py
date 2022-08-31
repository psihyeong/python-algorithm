# BOJ 7562번 나이트의 이동
from collections import deque

def bfs(a,b):
    que = deque()
    que.append((a,b))
    while que:
        y,x = que.popleft()
        # 나이트가 이동할 수 있는 경우의 수
        for dy,dx in [(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(-1,2),(-2,1),(2,-1)]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < l and 0 <= nx < l and visited[ny][nx] == 0:
                que.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1

TC = int(input())
for tc in range(1,TC+1):
    l = int(input())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    px, py = map(int,input().split())
    gx, gy = map(int,input().split())

    bfs(py,px)
    # 나이트 현재 칸과 이동하려는 칸이 같으면 0
    if py==gy and px==gx:
        print(0)
    else:
        print(visited[gy][gx])
