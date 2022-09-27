# SWEA 1865번 동철이의 일 분배

def dfs(depth, val):
    global result
    if val <= result:
        return
     
    if depth == N:
        if val > result:
            result = val
     
    else:
        for i in range(N):
            if not visited[i]:
                new_val = val*float(graph[depth][i]/100)
                visited[i] = True
                dfs(depth+1,new_val)
                visited[i] = False
 
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 0
    dfs(0,1)
    print(f'#{tc} {result*100:.6f}')
