# BOJ 5427번 불
from collections import deque

TC = int(input())
for tc in range(1,TC+1):
    w, h = map(int,input().split())
    mapp = []
    run = deque()
    r_visited = [[0 for _ in range(w)] for _ in range(h)]
    fire = deque()
    f_visited = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if tmp[j] == '@':
                run.append((i,j))

            elif tmp[j] == '*':
                fire.append((i,j))
        mapp.append(tmp)

    while fire:
        y,x = fire.popleft()
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w and (mapp[ny][nx] == '.' or mapp[ny][nx] == '@'):
                if f_visited[ny][nx] == 0:
                    f_visited[ny][nx] = f_visited[y][x] + 1
                    fire.append((ny,nx))

    while run:
        y,x = run.popleft()
        for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w and mapp[ny][nx] == '.':
                if r_visited[ny][nx] == 0 and f_visited[ny][nx] >= (r_visited[y][x] + 1):
                    r_visited[ny][nx] = r_visited[y][x] + 1
                    run.append((ny,nx))

    result = 0
    for i in range(w):
        if r_visited[0][i] > result:
            result = r_visited[0][i]
        if r_visited[h-1][i] > result:
            result = r_visited[h-1][i]

    for i in range(h):
        if r_visited[i][0] > result:
            result = r_visited[i][0]
        if r_visited[i][w-1] > result:
            result = r_visited[i][w-1]

    if result == 0:
        print('IMPOSSIBLE')
    else:
        print(result+1)
