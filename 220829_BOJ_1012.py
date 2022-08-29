# BOJ 1012번 유기농 배추

T = int(input())
for _ in range(T):
    W,H,K = map(int,input().split())
    farm = [[0 for _ in range(W)] for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    case = []
    for _ in range(K):
        x,y = map(int,input().split())
        farm[y][x] = 1
        case.append((y,x))

    stack = []
    result = 0
    # 모든 배추자리 중
    for i in case:
        # 방문하지 않은 배추만 DFS 시작점으로 삽입
        if not visited[i[0]][i[1]]:
            stack.append((i[0],i[1]))
            # 인접해있는 배추들은 방문처리
            while stack:
                y,x = stack.pop()
                visited[y][x] = True
                for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
                    ny = y+dy
                    nx = x+dx
                    if 0<=ny<H and 0<=nx<W and farm[ny][nx] == 1:
                        if not visited[ny][nx]:
                            stack.append((ny,nx))
            
            # 인접한 배추 탐색이 끝나면 배추흰지렁이 추가
            result += 1
    print(result)
