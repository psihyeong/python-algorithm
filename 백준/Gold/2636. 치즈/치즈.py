# BOJ 2636번 치즈

from collections import deque
# 공기와 맞닿은 가장자리 치즈를 녹이는 BFS
def melting_bfs(y,x):
    visited = [[0 for _ in range(W)] for _ in range(H)]
    q = deque()
    # 시작점은 임의의 바깥 공기
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
                # 공기면, 계속 너비우선 탐색
                if graph[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                # 최초로 만난 치즈면 녹이기
                elif graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    visited[ny][nx] = 1

# 남아있는 치즈의 개수를 반환하는 함수
def remain_cheeze():
    tmp = 0
    for row in graph:
        tmp += sum(row)

    return tmp

H, W = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(H)]
melting_cnt = 0
last_cheeze = 0
while True:
    # 남은 치즈가 없으면 종료
    if remain_cheeze() == 0:
        break
    # 종료 직전의 남은 치즈의 갯수가 최종 갱신됨
    else:
        last_cheeze = remain_cheeze()
        
    # 공기면, 해당 위치에서 BFS
    for i in range(H):
        is_melted = 0
        for j in range(W):
            if graph[i][j] == 0:
                melting_bfs(i,j)
                is_melted = 1
                break
        if is_melted:
            break
    # 녹인 횟수 +1
    melting_cnt += 1

print(melting_cnt)
print(last_cheeze)