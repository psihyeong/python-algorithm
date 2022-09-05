# BOJ 1780번 종이의 개수

# 종이의 시작좌표와 마지막좌표
def ispaper(sy,sx,ey,ex):
    # 원소가 한개면 종이로 취급
    if sy==ey and sx==ex:
        result[paper[sy][sx]+1] += 1
        return
    # 종이가 같은 수로 되어있는지 체크
    check = paper[sy][sx]
    notallsame = 0
    for i in range(sy,ey+1):
        for j in range(sx,ex+1):
            if check != paper[i][j]:
                notallsame = 1
                break
        if notallsame:
            break
    # 모두 같지 않다면 나눠서 함수호출
    if notallsame:
        tmp = (ey-sy+1)//3
        for i in range(sy,ey+1,tmp):
            for j in range(sx,ex+1,tmp):
                ispaper(i,j,i+tmp-1,j+tmp-1)
    # 같다면 종이로 취급
    else:
        result[paper[sy][sx] + 1] += 1
        return

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
sy,sx,ey,ex = 0,0,N-1,N-1
result = [0,0,0]


ispaper(sy,sx,ey,ex)
for i in result:
    print(i)
