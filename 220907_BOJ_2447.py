# BOJ 2447번 별 찍기 - 10

def stars(y,x,n):
    # 별 3개짜리면 가운데만 공백으로 바꿔주기
    if n == 3:
        starmap[y+1][x+1] = ' '
        return
    # 9등분
    for ni in range(3):
        for nj in range(3):
            # 가운데면 center 함수 호출
            if ni == 1 and nj == 1:
                center(y+ni*n//3,x+nj*n//3,n//3)
            # 나머지는 재귀호출
            else:
                stars(y+ni*n//3,x+nj*n//3,n//3)
    return

# 모두 공백으로 바꿔주기
def center(y,x,n):
    for i in range(n):
        for j in range(n):
            starmap[y+i][x+j] = ' '
    return

N = int(input())
# 시작은 모두 별
starmap = [['*' for _ in range(N)] for _ in range(N)]

stars(0,0,N)

for row in starmap:
    print(''.join(row))
