# BOJ 14503번 로봇 청소기
# 시뮬레이션
from collections import deque

# 왼쪽 방향을 구하는 함수
def left_d(d):
    if d > 0:
        return d-1
    else:
        return 3

# 청소가 가능한 좌표인지 확인하는 함수
def cleaning(y,x):
    if 0<= y < H and 0<= x < W and graph[y][x] == 0:
        return True
    else:
        return False

# 청소 시작
def bfs(y,x,d):
    global result
    q = deque()
    # 시작점
    q.append((y,x,d,0))
    graph[y][x] = 2
    # 탐색
    while q:
        # 좌표, 방향, 돈 횟수
        y, x, d, cir = q.popleft()
        # 4번 돌았으면 후진하는 경우
        if cir == 4:
            ny = y - dir[d][0]
            nx = x - dir[d][1]
            # 후진가능하면
            if graph[ny][nx] != 1:
                # 후진
                q.append((ny,nx,d,0))
                continue
            # 불가능하면 탐색 끝
            else:
                return
        # 왼쪽 방향
        nd = left_d(d)
        # 좌표 구해서
        ny = y + dir[nd][0]
        nx = x + dir[nd][1]
        # 청소가능하면
        if cleaning(ny,nx):
            # 청소
            graph[ny][nx] = 2
            # 청소 횟수 더해주고
            result += 1
            # 이동
            q.append((ny,nx,nd,0))
        # 불가능하면
        else:
            # 회전
            q.append((y,x,nd,cir+1))


H, W = map(int,input().split())
ny,nx,d = map(int,input().split())
dir = [(-1,0),(0,1),(1,0),(0,-1)]
graph = [list(map(int,input().split())) for _ in range(H)]
visited = [[0 for _ in range(W)] for _ in range(W)]
result = 1
bfs(ny,nx,d)
print(result)