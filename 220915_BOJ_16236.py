# BOJ 16236번 아기 상어
from collections import deque
import heapq

# 가장 가까운 물고기 하나를 먹는 데 걸리는 시간 더 해주고, 먹은 위치를 반환하는 bfs
def bfs(h,w,size):
    global result
    que = deque()
    que.append((h,w))
    visited[h][w] = 0
    # 내가 먹을 수 있는 물고기의 정보를 담는 tmp
    tmp = []
    while que:
        y,x = que.popleft()
        for dy,dx in [(-1,0),(0,-1),(0,1),(1,0)]:
            ny = y + dy
            nx = x + dx
            # 상어보다 사이즈가 크지 않은 물고기를 지나면서
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and graph[ny][nx] <= size:
                que.append((ny, nx))
                # 거리를 계산
                visited[ny][nx] = visited[y][x] + 1
                # 만약 몸집보다 작은 물고기다, 먹을 수 있는 물고기면, (거리, y, x 좌표)를 tmp에 삽입
                if 0 < graph[ny][nx] < size:
                    # 거리, y, x 순으로 내림차순 정렬을 위해 우선순위 큐 사용
                    heapq.heappush(tmp,(visited[ny][nx],ny,nx))
    # 주변에 먹을 물고기 없으면, 엄마 상어의 도움이 필요할 때
    if len(tmp) == 0:
        return -1, -1
    # result에 거리 더 해주고, yx위치 반환
    else:
        sec = tmp[0][0]
        ny = tmp[0][1]
        nx = tmp[0][2]
        result += sec
        graph[ny][nx] = 0
        return ny, nx

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
# 물고기의 수
fishs = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            y, x = i, j
            graph[i][j] = 0
        elif graph[i][j] > 0:
            fishs += 1
# 상어의 몸집
shark = 2
# 결과
result = 0
# 상어가 먹은 물고기 수
eat = 0
# 물고기 개수 만큼 진행
for _ in range(fishs):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    y,x = bfs(y,x,shark)

    # bfs가 한 번 돌 때 한마리를 먹은 것으로 처리
    eat += 1
    # 물고기를 몸집만큼 먹었다면
    if eat == shark:
        # 몸집이 커지고
        shark += 1
        # 먹은 물고기 수 초기화
        eat = 0
    # 아무리 돌아봐도 먹을 것이 없을 때, 엄마 상어의 도움이 필요할 때
    if y == -1 and x == -1:
        break

print(result)
