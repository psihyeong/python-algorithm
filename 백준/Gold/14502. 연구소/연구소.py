# BOJ 14502번 연구소

from collections import deque

# 안전영역의 수를 반환하는 bfs
def infect_bfs():
    infect = 0      # 감염자 수
    visited = [[0 for _ in range(W)] for _ in range(H)]
    q = deque()
    # 바이러스 위치부터 출발해서
    for y,x in virus:
        q.append((y,x))
        visited[y][x] = True
        while q:
            y,x = q.popleft()
            for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                ny = y + dy
                nx = x + dx
                # 방문하지 않았고, 빈 칸이면 감염
                if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and graph[ny][nx] == 0:
                    q.append((ny,nx))
                    visited[ny][nx] = True
                    infect += 1
    # 최초 빈칸 수 - 감염자 수 - 세워진 벽 3 = 안전영역
    return is_empty-infect-3

# 벽 3개의 위치를 조합하는 함수
def comb(startwith,lst):
    global result
    # 벽이 3개가 되면
    if len(lst) == 3:
        # 벽을 세우고
        for y, x in lst:
            graph[y][x] = 1
        # 안전영역을 구한 뒤 최댓값 갱신
        tmp = infect_bfs()
        result = max(result, tmp)
        # 벽 제거
        for y, x in lst:
            graph[y][x] = 0
        return
    
    else:
        for i in range(startwith,is_empty):
            lst.append(sub[i])
            comb(i+1,lst)
            lst.pop()


H,W = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]

sub = []        # 벽이 세워질 수 있는 모든 빈 칸 좌표 리스트
virus = []      # 바이러스들의 좌표 리스트
for i in range(H):
    for j in range(W):
        if graph[i][j] == 0:
            sub.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))
# 최초 빈 칸의 수
is_empty = len(sub)
result = 0
tmp_lst = []
comb(0,tmp_lst)
print(result)