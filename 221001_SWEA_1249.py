# SWEA 1249번 보급로

from collections import deque

def bfs(x, y, large, time, visited):
    queue = deque()
    queue.append((x, y))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < large and 0 <= ny < large:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + graph[nx][ny]
                    queue.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + graph[nx][ny]:
                        time[nx][ny] = time[x][y] + graph[nx][ny]
                        queue.append((nx, ny))

    return time[large - 1][large - 1]


for tc in range(1, int(input()) + 1):
    large = int(input())
    graph = [list(map(int, input())) for _ in range(large)]
    time = [[0] * large for _ in range(large)]
    visited = [[0] * large for _ in range(large)]

    print(f"#{tc} {bfs(0, 0, large, time, visited)}")
