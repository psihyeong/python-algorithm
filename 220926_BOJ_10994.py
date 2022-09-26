# BOJ 10994번 별 찍기 - 19

# 바깥 테두리부터 별을 찍는 함수
def star(n, y, x):
    if n == 1:
        stars[y][x] = '*'
        return

    else:
        # 해당 테두리의 길이
        length = 4*(n-1) + 1
        # 테두리 별 찍기
        for i in range(length):
            # 윗쪽 테두리
            stars[y][x+i] = '*'
            # 왼쪽 테두리
            stars[y+i][x] = '*'
            # 아래쪽 테두리
            stars[y+length-1][x+i] = "*"
            # 오른쪽 테두리
            stars[y+i][x+length-1] = "*"

        # 다음 테두리 호출
        star(n-1, y+2, x+2)

N = int(input())
# 가장 큰 테두리의 길이를 기준으로 리스트 생성
stars = [[' ' for _ in range(4*(N-1) + 1)] for _ in range(4*(N-1) + 1)]
star(N,0,0)
for row in stars:
    print(''.join(row))
