# SWEA 10966번 물놀이를 가자
from collections import deque
TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    result = [[-1 for _ in range(M)] for _ in range(N)]
    water = deque()
#     mapp = [list(input()) for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if mapp[i][j] == 'W':
#                 water.append((i, j))
#                 result[i][j] = 0

# 메모리 초과 방지를 위해서 아래와 같은 코드로 대체.
    for i in range(N):
        row = input()
        for j in range(len(row)):
            if row[j] == 'W':
                water.append((i, j))
                result[i][j] = 0
# 위 코드는 따로 지도 그래프를 만들지 않아도 됨. 메모리 감소
    result_val = 0
    # BFS
    while water:
        wy,wx = water.popleft()
        for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
            nx = dx+wx
            ny = dy+wy
         	# 범위를 벗어나지 않으면서
            if 0<=nx<M and 0<=ny<N:
            	if result[ny][nx] == -1:
                    # 방문값이 -1이면서(W에서 0 부터 출발하지만, L을 확인하고 싶을 때)
                    water.append((ny,nx))
                    result[ny][nx] = result[wy][wx] + 1
        result_val += result[wy][wx]

    print(f'#{tc} {result_val}')
