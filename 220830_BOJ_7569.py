# BOJ 7569번 토마토

from collections import deque
import sys
input = sys.stdin.readline

W,H,K = map(int,input().split())
tomato = []
baby = 0
# 큐에 최초 익은 토마토 좌표 담기
queue = deque()
for k in range(K):
    tmp = []
    for i in range(H):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for j in range(W):
            if tmp[i][j]==1:
                queue.append((k,i,j))
            # baby는 안 익은 토마토 개수
            elif tmp[i][j]==0:
                baby += 1
    tomato.append(tmp)
    
# 3차원 BFS
grown = 0
result = 1
while queue:
    s,y,x = queue.popleft()
    for ds,dy,dx in [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        ns = s+ds
        ny = y+dy
        nx = x+dx
        if 0<=ns<K and 0<=ny<H and 0<=nx<W and tomato[ns][ny][nx] == 0:
            queue.append((ns,ny,nx))
            # 익은 토마토 개수
            grown += 1
            # 거리 = 익는 데 걸리는 최소 일 수
            tomato[ns][ny][nx] = tomato[s][y][x] + 1
            # result 갱신
            if tomato[ns][ny][nx] > result:
                result = tomato[ns][ny][nx]
                
# 안 익은 토마토의 개수와 익은 토마토의 개수가 같다면 다 익은 것이므로 result 출력                                   
if baby == grown:
    print(result-1)
# 안 익은게 존재하면 -1
else:
    print(-1)
