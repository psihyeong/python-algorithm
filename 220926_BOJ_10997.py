# BOJ 10997번 별 찍기 - 22

# 오른쪽 윗 모서리부터 별을 찍는 함수
def star(n, y, x):
    if n == 1:
        stars[y][x] = '*'
        return
    # n이 2일때 추가적으로 찍히는 별 처리
    if n == 2:
        stars[y + 3][x - 2] = '*'
        stars[y + 4][x - 2] = '*'
    # 해당 테두리의 너비
    width = 4 * (n - 1) + 1
    # 높이
    height = 4 * n - 1

    # 두번째 줄 공백제거
    if n == N:
        for i in range(width-1):
            stars[y+1][x-i] = ''

    # 테두리 별 찍기
    for i in range(width):
        # 윗쪽 테두리
        stars[y][x-i] = '*'
        # 아래쪽
        stars[y+height-1][x-i] = '*'

    for i in range(height):
        # 왼쪽
        stars[y+i][x-width+1] = '*'

    # 오른쪽 테두리
    for i in range(2,height):
        stars[y+i][x] = '*'
    # 추가 별 찍기
    stars[y+2][x-1] = '*'
    # 다음 테두리 호출
    star(n-1, y+2, x-2)

N = int(input())
# 가장 큰 테두리의 길이를 기준으로 리스트 만들기
stars = [[' ' for _ in range(4*(N-1) + 1)] for _ in range(4*N - 1)]
star(N,0,4*(N-1))
for row in stars:
    print(''.join(row))
