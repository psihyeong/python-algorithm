# BOJ 7569번 토마토

from collections import deque

W,H,K = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(H)] for _ in range(K)]

queue = deque()
for k in range(K):
    for i in range(H):
        for j in range(W):
            if tomato[k][i][j] == 1:
                queue.append((k,i,j))
            while queue:
                s,y,x = queue.popleft()
                for ds,dy,dx in [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
                    ns = s+ds
                    ny = y+dy
                    nx = x+dx
                    if 0<=ns<K and 0<=ny<H and 0<=nx<W:
                        if tomato[ns][ny][nx] == 0:
                            queue.append((ns,ny,nx))
                            tomato[ns][ny][nx] = tomato[s][y][x] + 1
result = 0
not_tomato = 1
for k in range(K):
    for i in range(H):
        for j in range(W):
            if tomato[k][i][j] == 0:
                not_tomato = 0
            else:
                if tomato[k][i][j] > result:
                    result = tomato[k][i][j]
if not_tomato:
    print(result-1)
else:
    print(-1)
