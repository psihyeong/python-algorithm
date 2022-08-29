# BOJ 10026번 적록색약

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
stack1 = []
stack2 = []
RB = 0
RGB = 0
# RGB 판별 DFS
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            stack1.append((i,j))
            while stack1:
                y, x = stack1.pop()
                visited[y][x] = True
                for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if graph[ny][nx] == graph[y][x]:
                            stack1.append((ny,nx))
            RGB += 1
# RB 판별 DFS
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            stack2.append((i,j))
            while stack2:
                y, x = stack2.pop()
                visited[y][x] = True
                for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if graph[y][x] == 'B' and graph[ny][nx] == 'B':
                            stack2.append((ny,nx))
                        if graph[y][x] in ['R','G'] and graph[ny][nx] in ['R','G']:
                            stack2.append((ny,nx))
            RB += 1


print(RGB,RB)
