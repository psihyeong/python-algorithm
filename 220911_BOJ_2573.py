# BOJ 2573번 빙산
from collections import deque

# 1년 동안 빙산을 녹이는 함수
def one_year_later():
    minus_lst = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            tmp = 0
            if ice[i][j]:
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < H and 0 <= nx < W and not ice[ny][nx]:
                        tmp += 1
            minus_lst[i][j] = tmp
    for i in range(H):
        for j in range(W):
            if ice[i][j] - minus_lst[i][j] > 0:
                ice[i][j] -= minus_lst[i][j]
            elif ice[i][j] - minus_lst[i][j] <= 0:
                ice[i][j] = 0
    return

# 빙산 한 덩이를 방문 처리해주는 함수
def ice_num_bfs(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and ice[ny][nx]:
                visited[ny][nx] = True
                q.append((ny,nx))
    return cnt

H, W = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(H)]


result = 0
while True:
    # 빙산 덩어리의 개수
    num = 0
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if ice[i][j] and not visited[i][j]:
                # 한 덩어리 마다 num에 +1
                num += ice_num_bfs(i,j)
    # 두 덩이 이상이면 반복문 종료
    if num > 1:
        break
    # 한 덩이면 일년 보내고 빙산 녹이기
    else:
        result += 1
        one_year_later()
    # 전부 다 녹을 때 까지 두 덩어리 이상으로 분리되지 않을 경우
    if num == 0:
        result = 0
        break

print(result)
