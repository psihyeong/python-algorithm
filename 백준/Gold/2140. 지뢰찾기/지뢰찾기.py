# BOJ 2140번 지뢰찾기

def find_sharp(y,x,n):
    global result
    real_mine = []
    sub_mine = []
    for dy,dx in [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        ny = y+dy
        nx = x+dx
        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] == '#':
                sub_mine.append((ny,nx))
            elif board[ny][nx] == '*':
                real_mine.append((ny,nx))
    if len(real_mine) == n:
        for y,x in sub_mine:
            board[y][x] = ' '
        return

    if n == len(sub_mine) + len(real_mine):
        for y,x in sub_mine:
            board[y][x] = '*'
            result += 1
        return

N = int(input())
board = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        if str.isdigit(board[i][j]):
            find_sharp(i,j,int(board[i][j]))

for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            result += 1

# for row in board:
#     print(*row)
print(result)

