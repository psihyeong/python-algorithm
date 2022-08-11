# SWEA 4875번 미로

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    miro = []
    for _ in range(N):
        tmp = list(map(int, input()))
        miro.append(tmp)

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    y, x = 0, 0
    for i in range(N):
        for j in range(N):
            if miro[j][i] == 3:
                y = j
                x = i
                break

    result = 0
    road = [[y, x]]

    # 갈 수 있는 길이 없을 때 종료.
    while road:
        # pop하면 방문한 것
        y, x = road.pop()
        miro[y][x] = 1

        for i in range(4):
        
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
                # 갈 수 있는 모든 길 road에 넣어주기
                if miro[ny][nx] == 0:
                    road.append([ny, nx])
                if miro[ny][nx] == 2:
                    result = 1
                    break

        # 중간에 미로를 탈출했다면 종료
        if result == 1:
            break

    print(f'#{tc} {result}')
