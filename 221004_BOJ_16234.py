# BOJ 16234번 인구 이동

from collections import deque

# 시작점부터 연합인 나라들을 방문처리하고, 연합인 나라들의 좌표 리스트와 이동 후 인구 수를 반환하는 함수
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    align = []
    align.append((i,j))
    all_align_people = world[i][j]
    all_align_cnt = 1
    while q:
        y,x = q.popleft()
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(world[ny][nx] - world[y][x]) <= R:
                    align.append((ny,nx))
                    all_align_cnt += 1
                    all_align_people += world[ny][nx]
                    q.append((ny,nx))
                    visited[ny][nx] = True
    return align, all_align_people//all_align_cnt

# 연합 나라들의 인구 수를 이동시키는 함수
def move(lst, val):
    for y,x in lst:
        world[y][x] = val

N, L, R = map(int,input().split())

world = [list(map(int,input().split())) for _ in range(N)] # 초기 나라
result = 0 # 인구 이동 일 수

# 반복문
while True:
    cnt = 0     # 연합국 탐색 횟수
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 탐색하지 않은 나라라면
            if not visited[i][j]:
                # 함수호출
                l,v = bfs(i,j)
                # 이동
                move(l,v)
                # 탐색 횟수 + 1
                cnt += 1
    # 탐색 횟수가 모든 나라의 수라면, 모든 나라가 1인 연합이라면,
    # 더 이상 인구이동이 불가하니 break
    if cnt == N**2:
        break
    # 인구이동이 가능하면 일 수 +1
    result += 1

print(result)
