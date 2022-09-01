# BOJ 5427번 불
from collections import deque

TC = int(input())
for tc in range(1,TC+1):
    w, h = map(int,input().split())
    mapp = []
    # 상근이가 달리는 시간 r_visited, 불이 번지는 시간 f_visited
    run = deque()
    r_visited = [[-1 for _ in range(w)] for _ in range(h)]
    fire = deque()
    f_visited = [[-1 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if tmp[j] == '@':
                run.append((i,j))
                r_visited[i][j] = 0
            elif tmp[j] == '*':
                fire.append((i,j))
                f_visited[i][j] = 0
        mapp.append(tmp)
    # 불이 번지는 시간을 구하는 bfs
    while fire:
        y,x = fire.popleft()
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w and mapp[ny][nx] != '#':
                if f_visited[ny][nx] == -1:
                    f_visited[ny][nx] = f_visited[y][x] + 1
                    fire.append((ny,nx))
    # 상근이가 달리는 시간을 구하는 bfs
    while run:
        y,x = run.popleft()
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w and mapp[ny][nx] == '.':
                # 해당 위치에 불이 번지는 시간보다 적은 시간에 상근이가 달릴 수 있는 경우, 불이 번지지 않은 자리(-1)일 경우
                if r_visited[ny][nx] == -1 and (f_visited[ny][nx] > r_visited[y][x]+1 or f_visited[ny][nx] == -1):
                    r_visited[ny][nx] = r_visited[y][x] + 1
                    run.append((ny,nx))
                    
    # 가장자리(출구) 중 가장 작은 값 출력
    result = int(1e9)
    for i in range(w):
        if r_visited[0][i] >= 0:
            if r_visited[0][i] < result:
                result = r_visited[0][i]
        if r_visited[h-1][i] >= 0:
            if r_visited[h-1][i] < result:
                result = r_visited[h-1][i]
    for i in range(h):
        if r_visited[i][0] >= 0:
            if r_visited[i][0] < result:
                result = r_visited[i][0]
        if r_visited[i][w-1] >= 0:
            if r_visited[i][w-1] < result:
                result = r_visited[i][w-1]
                
    # 탈출하지 못했다면
    if result == int(1e9):
        print('IMPOSSIBLE')
    # 탈출했다면
    else:
        print(result+1)
