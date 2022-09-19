# BOJ 1074번 Z

def divide(y,x,N):
    global num
    # 크기가 2X2인 경우
    if N == 2:
        for i in range(2):
            for j in range(2):
                if r == y+i and c == x+j:
                    # 결과 출력
                    print(num)
                num += 1
    else:
        # 사분면을 찾고 방문순서 갱신
        half = N//2
        # 1사분면
        if y <= r < y + half and x <= c < x + half:
            divide(y,x,half)
        # 2사분면
        elif y <= r < y + half and x+half <= c < x+N:
            num += (half**2)
            divide(y, x+half, half)
        # 3사분면
        elif y + half <= r < y+N and x <= c < x + half:
            num += (half**2) * 2
            divide(y+half, x, half)
        # 4사분면
        else:
            num += (half**2) * 3
            divide(y+half, x+half, half)

N, r, c = map(int,input().split())
num = 0
divide(0,0,2**N)
