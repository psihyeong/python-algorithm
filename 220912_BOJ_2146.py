# BOJ 2146번 다리 만들기
from collections import deque

# 육지의 번호를 최신화 해주는 함수
def num_bfs(y,x,n):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    mapp[y][x] = n
    while q:
        qy,qx = q.popleft()
        for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)]:
            ny = qy + dy
            nx = qx + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and mapp[ny][nx] != 0:
                visited[ny][nx] = True
                # 육지 번호 최신화
                mapp[ny][nx] = n
                q.append((ny,nx))

# 육지에서 육지로 가는 최단 경로를 구하는 bfs
def bfs(y,x,my_num):
    global result
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    while q:
        qy,qx = q.popleft()
        for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)]:
            ny = qy + dy
            nx = qx + dx
            if 0 <= ny < N and 0 <= nx < N:
                # 다리 길이를 더 해가다가 다른 육지면
                if mapp[ny][nx] > 0 and mapp[ny][nx] != my_num:
                    # 육지까지 거리와 result를 비교해서 최솟값 갱신
                    if result > visited[qy][qx]:
                        result = visited[qy][qx]
                # 다리 놓기
                elif not visited[ny][nx] and mapp[ny][nx] == 0:
                    visited[ny][nx] = visited[qy][qx] + 1
                    q.append((ny,nx))

N = int(input())
mapp = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
result = int(1e9)
# 육지 번호 최신화
n = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and mapp[i][j] == 1:
            num_bfs(i,j,n)
            n += 1

# 육지에서 최단 거리 구하기
for i in range(N):
    for j in range(N):
        if mapp[i][j] != 0:
            visited = [[0 for _ in range(N)] for _ in range(N)]
            bfs(i,j,mapp[i][j])

print(result-1)
