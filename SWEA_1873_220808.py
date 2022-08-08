# SWEA 1873번 상호의 배틀필드

TC = int(input())
for tc in range(1,TC+1):
    H, W = map(int, input().split())
    mapp = [list(map(str,input())) for row in range(H)]
    N = int(input())
    command = list(map(str,input()))
    dir = ''
    # 탱크의 현재위치
    x, y = 0,0
    direction = ['<','>','^','v']
    # 탱크의 현재위치와 방향 찾기
    for i in range(H):
        for j in range(W):
            if mapp[i][j] in direction:
                y,x = i, j
                dir = mapp[i][j]
    
    for i in range(N):
     	
        if command[i] == 'S':
            if dir == '^':
                # 윗방향 요소들이 
                for j in range(y-1,-1,-1):
                    # 벽돌이면 평지로
                    if mapp[j][x] == '*':
                        mapp[j][x] = '.'
                        break
                    # 강철이면 무반응
                    elif mapp[j][x] == '#':
                        break
                        
            elif dir == 'v':
                for j in range(y+1,H):
                    if mapp[j][x] == '*':
                        mapp[j][x] = '.'
                        break
                    elif mapp[j][x] == '#':
                        break
                        
            elif dir == '>':
                for j in range(x+1,W):
                    if mapp[y][j] == '*':
                        mapp[y][j] = '.'
                        break
                    elif mapp[y][j] == '#':
                        break
                        
            elif dir == '<':
                for j in range(x-1,-1,-1):
                    if mapp[y][j] == '*':
                        mapp[y][j] = '.'
                        break
                    elif mapp[y][j] == '#':
                        break
                        
		# 방향 커맨드 입력시
        elif command[i] == 'U':
            # 방향 바꿔주고
            dir = '^'
            mapp[y][x] = dir
            # 이동할 공간이
            ny = y - 1
            # 벗어나지 않았고
            if 0 <= ny < H:
                # 평지면
                if mapp[ny][x] == '.':
                    # 이동
                    mapp[ny][x], mapp[y][x] = mapp[y][x], mapp[ny][x]
                    y = ny

        elif command[i] == 'D':
            dir = 'v'
            mapp[y][x] = dir
            ny = y + 1
            if 0 <= ny < H:
                if mapp[ny][x] == '.':
                    mapp[ny][x], mapp[y][x] = mapp[y][x], mapp[ny][x]
                    y = ny
        
        elif command[i] == 'R':
            dir = '>'
            mapp[y][x] = dir
            nx = x + 1
            if 0 <= nx < W:
                if mapp[y][nx] == '.':
                    mapp[y][nx], mapp[y][x] = mapp[y][x], mapp[y][nx]
                    x = nx
        
        elif command[i] == 'L':
            dir = '<'
            mapp[y][x] = dir
            nx = x - 1
            if 0 <= nx < W:
                if mapp[y][nx] == '.':
                    mapp[y][nx], mapp[y][x] = mapp[y][x], mapp[y][nx]
                    x = nx

    print(f'#{tc}',end=' ')
    for row in mapp:
        print(''.join(row))
