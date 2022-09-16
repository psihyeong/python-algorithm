# SWEA 2117번 홈 방범 서비스

from collections import deque

# dis범위 내에 들어가는 집의 갯수를 반환하는 함수 bfs
def bfs(y,x,dis):
    q = deque()
    q.append((y,x))
    inhome = 0
    if homes[y][x]:
        inhome += 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 원점에서의 거리 최신화
                visited[ny][nx] = visited[y][x] +1
                # 거리가 범위안에 들어오면
                if visited[ny][nx] <= dis:
                    # 큐에 삽입
                    q.append((ny, nx))
                    # 집이면 결과값에 +1
                    if homes[ny][nx]:
                        inhome += 1
    return inhome
 
TC = int(input())
for tc in range(1, TC+1):
    N, fee = map(int,input().split())
    homes = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for r in range(1, N+2):
        oper = (r**2 + (r-1)**2)
        for i in range(N):
            for j in range(N):
                # 해당 범위에 들어가는 집의 갯수
                able_home = bfs(i,j,r)
                # 방범 서비스를 제공하는게 흑자면
                if able_home*fee - oper >= 0:
                    # 집의 갯수 최댓값 최신화
                    if result < able_home:
                        result = able_home
    print(f'#{tc} {result}')
