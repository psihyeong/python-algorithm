# BOJ 14500번 테트로미노

def dfs(idy,idx, bl, curS):
    global result
    # bl = block length
    # 가지치기
    if (result - curS) > (n-bl)*max_val:
        return

    if bl == n:
        if curS > result:
            result = curS
        return

    else:
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = idy + dy
            nx = idx + dx
            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx]:
                    tmp = curS+ graph[ny][nx]
                    # 'ㅓ' 모양 탐색을 위해 3번째값까지 더하고 2번째 값으로 복귀
                    if bl == 2:
                        visited[ny][nx] = True
                        dfs(idy, idx, bl + 1, tmp)
                        visited[ny][nx] = False
                    # 나머지 모양 탐색
                    visited[ny][nx] = True
                    dfs(ny, nx, bl + 1, tmp)
                    visited[ny][nx] = False

N, M = map(int,input().split())
n = 4
result = 0
graph = [list(map(int,input().split())) for _ in range(N)]
max_val = 0

for row in graph:
    if max(row) > max_val:
        max_val = max(row)

visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False

print(result)
