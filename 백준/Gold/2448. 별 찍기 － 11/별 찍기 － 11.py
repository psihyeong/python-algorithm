# BOJ 2448번 별 찍기 - 11
N = int(input())
def stars(y,x,n):
    # 3줄짜리면 꼭지점 밑에만 공백으로 바꿔주기
    if n == 3:
        starmap[y+1][x] = ' '
        return
    # 가운데 공백 처리
    tmp = n//2
    for i in range(n-1,tmp-1,-1):
        for j in range(n-i):
            starmap[y+i][x+j] = ' '
            starmap[y+i][x-j] = ' '
    # 3개의 꼭지점으로 나누기
    stars(y,x,tmp)
    stars(y+tmp,x-tmp,tmp)
    stars(y+tmp,x+tmp,tmp)

    return

# 일단 삼각산을 하나 만들자
starmap = []
for i in range(1,N+1):
    tmp = [' ' for _ in range(N-i)] + ['*' for _ in range(1+2*(i-1))] + [' ' for _ in range(N-i)]
    starmap.append(tmp)
# 꼭지점으로 함수 시작
stars(0,N-1,N)

for row in starmap:
    print(''.join(row))