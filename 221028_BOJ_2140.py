# BOJ 2140번 지뢰찾기
# 그리디, 구현

# 숫자 칸 인접의 지뢰를 찾는 함수
def find_mine(y,x,n):
    global result
    # 확정 지뢰 칸 좌표 리스트
    real_mine = []
    # 지뢰 후보 칸 좌표 리스트
    sub_mine = []
    # 8방 탐색
    for dy,dx in [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        ny = y+dy
        nx = x+dx
        if 0 <= ny < N and 0 <= nx < N:
            # 지뢰 후보 칸이면
            if board[ny][nx] == '#':
                sub_mine.append((ny,nx))
            # 확정 지뢰 칸이면
            elif board[ny][nx] == '*':
                real_mine.append((ny,nx))

    # 숫자만큼 확정 지뢰를 모두 찾았으면,
    if len(real_mine) == n:
        # 나머지 지뢰 후보 칸은 모두 빈 칸
        for y,x in sub_mine:
            board[y][x] = ' '
        return
    # 확정 지뢰 칸 + 후보 지뢰 칸 수가 숫자만큼이라면
    if n == len(sub_mine) + len(real_mine):
        # 지뢰 후보 칸들은 모두 확정 지뢰, 지뢰를 찾음
        for y,x in sub_mine:
            board[y][x] = '*'
            # 지뢰를 찾았으므로 +1
            result += 1
        return

N = int(input())
board = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        # 숫자칸이면
        if str.isdigit(board[i][j]):
            # 지뢰찾기
            find_mine(i,j,int(board[i][j]))

# 최댓값을 위해 마지막까지 남은 지뢰 후보는 모두 지뢰
for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            result += 1

print(result)