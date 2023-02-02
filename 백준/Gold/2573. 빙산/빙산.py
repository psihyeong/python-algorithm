# BOJ 17135번 캐슬 디펜스
from collections import deque

def asd(arr):
    global cnt
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == False:
                visited[i][j] = True
                cnt += 1
                q = deque()
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx = xx + x
                        ny = yy + y
                        if 0<=nx<N and 0<=ny<M and arr[nx][ny] != 0 and visited[nx][ny] == False:
                            q.append((nx, ny))
                            visited[nx][ny] = True
    return 0

def find_zero(lst):
    zero_lst = deque()
    while lst:
        zero_cnt = 0
        x, y = lst.popleft()
        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = xx + x
            ny = yy + y
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                zero_cnt += 1
        zero_lst.append(zero_cnt)
    return zero_lst



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
melt_cnt = 0


while True:
    cnt = 0
    asd(arr)
    lst = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                lst.append((i, j))
    zero_lst = find_zero(lst)
    zxc = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                if arr[i][j] - zero_lst[zxc] < 0:
                    arr[i][j] = 0
                    zxc += 1
                else:
                    arr[i][j] -= zero_lst[zxc]
                    zxc += 1
    melt_cnt += 1
    if cnt > 1:
        break
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                zero_cnt += 1
    if zero_cnt == N*M:
        melt_cnt = 1
        break
print(melt_cnt-1)
