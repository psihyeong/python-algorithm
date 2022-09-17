# SWEA 4615번 재미있는 오셀로 게임

from collections import deque
# 돌을 놓을 때
def su(y,x,stone):
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]:
        # correct 함수를 통해
        able, length = correct(y,x,dy,dx,stone)
        # 놓아도 되는 수, 가능한 수면
        if able:
            # 길이만큼 돌을 바꿔줌
            for i in range(0,length+2):
                ny = y + dy*i
                nx = x + dx*i
                graph[ny][nx] = stone

# 시작점부터 한 방향으로 반대돌을 찾는 함수
def correct(y,x,dy,dx,stone):
    q = deque()
    q.append((y,x))
    length = 0
    while q:
        y,x = q.popleft()
        ny = dy + y
        nx = dx + x
        if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] != 0 :
            if graph[ny][nx] != stone:
                length += 1
                q.append((ny,nx))
            if graph[ny][nx] == stone and length > 0:
                return (1,length)
        else:
            break

    return (0,length)

TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int,input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph[N//2][N//2] = 2
    graph[N//2-1][N//2-1] = 2
    graph[N // 2-1][N // 2] = 1
    graph[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        x, y, stone = map(int,input().split())
        su(y-1,x-1,stone)

    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                black += 1
            elif graph[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')
