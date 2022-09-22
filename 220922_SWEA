# SWEA 1247번 최적 경로

def dfs(y,x,val,depth):
    global result
    # 마지막 고객까지 방문했다면
    if depth == N:
        # 집으로 가고
        val += abs(home_y - y)
        val += abs(home_x - x)
        # 결과값 갱신
        result = min(result,val)
        return
    else:
        # 고객들중
        for i in range(N):
            # 방문 안 한 고객이면
            if not visited[i]:
                ny, nx = clients[i][0], clients[i][1]
                dis = abs(ny-y)+abs(nx-x)
 
                # 방문해주고
                visited[i] = True
                # 거리 더 해주고, 만난 손님 수 +1
                dfs(ny,nx,val+dis,depth+1)
                # 백트래킹 후처리
                visited[i] = False
 
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    tmp = list(map(int,input().split()))
    company_x, company_y, home_x, home_y = tmp[0], tmp[1], tmp[2], tmp[3]
    clients = []
    for i in range(4,N*2+4,2):
        clients.append((tmp[i + 1], tmp[i]))
    result = int(1e9)
    # 고객별 방문 유무
    visited = [0 for _ in range(N)]
    # 회사에서 출발
    dfs(company_y, company_x, 0, 0)
    print(f'#{tc} {result}')
