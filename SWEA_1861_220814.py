# SWEA 1861번 정사각형 방
from collections import deque

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    
    rooms = [list(map(int,input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    max_value = 0
    result_room = 0
    # 모든 좌표
    for y in range(N):
        for x in range(N):
    
            check = deque()
            check.append((y,x))
            check_value = 0
            
            while check:
                check_y, check_x = check.popleft()
                check_value += 1
                
                for dir in range(4):
                    nx = check_x+dx[dir]
                    ny = check_y+dy[dir]
                    if 0 <= nx < N and 0 <= ny < N:
                        if rooms[ny][nx] == rooms[check_y][check_x] + 1:
                            check.append((ny,nx))
            
            # 최댓값 갱신, 방 번호 갱신
            if check_value > max_value:
                max_value = check_value
                result_room = rooms[y][x]
            # 최댓값이 같으면, 작은 방 번호 갱신    
            elif check_value == max_value:
                if result_room > rooms[y][x]:
                    result_room = rooms[y][x]


    print(f'#{tc} {result_room} {max_value}')
