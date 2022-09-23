# SWEA 2819번 격자판의 숫자 이어 붙이기
 
def dfs(y,x,val):
    if len(val) == 7:
        result.append(val)
        return
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 4 and 0 <= nx < 4 and len(val) <= 6:
            dfs(ny,nx,val + graph[ny][nx])
 
 
TC = int(input())
for tc in range(1,TC+1):
    graph = [list(map(str,input().split())) for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            tmp = graph[i][j]
            dfs(i,j,tmp)
    print(f'#{tc} {len(set(result))}')
