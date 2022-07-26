# SWEA 1954.달팽이 숫자

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dal = [[0] * N for _ in range(N)]
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    x, y, direct = 0, 0, 0
    for i in range(1,N**2+1):
        dal[y][x] = i
        y += direction[direct][0]
        x += direction[direct][1]
        if x >= N or x < 0 or y < 0 or y >= N or dal[y][x] != 0:
            y -= direction[direct][0]
            x -= direction[direct][1]
            direct = (direct+1)%4
            y += direction[direct][0]
            x += direction[direct][1]
    print(f"#{tc}")
    for i in dal:
        print(' '.join(map(str,i)))
