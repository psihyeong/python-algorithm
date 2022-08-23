# SWEA 4881번 배열 최소 합

def dfs(y,cost):
    global result
    # 높이가 N이 되기 전에 최솟값을 넘어버리면 해당 루트 종료.
    if cost > result:
        return
    # N이면 최솟값 갱신
    if y == N:
        if result > cost:
            result = cost
        return result
    for i in range(N):
        # 겹치지 않게 내려가기 위해
        if not visited[i]:
            visited[i] = True
            dfs(y+1,cost+arr[y][i])
            # 다른 경우도 봐야하기 때문에 False로 초기화
            visited[i] = False

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    result = int(1e9)

    dfs(0,0)
    print(f'#{tc} {result}')
