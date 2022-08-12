# SWEA 12712번 파리퇴치3

def shot(y, x, n):
    result1 = 0
    result2 = 0
    for i in range(-n, n + 1):
        if 0 <= y+i < N and 0 <= x < N:
            result1 += flys[y+i][x]
        if 0 <= y < N and 0 <= x+i < N:
            result1 += flys[y][x+i]
 
    result1 -= flys[y][x]
 
    for i in range(-n, n + 1):
        if 0 <= y + i < N and 0 <= x+i < N:
            result2 += flys[y+i][x+i]
        if 0 <= y - i < N and 0 <= x + i < N:
            result2 += flys[y-i][x+i]
 
    result2 -= flys[y][x]
 
    return result1, result2
 
TC = int(input())
for tc in range(1,TC+1):
    N, power = map(int,input().split())
 
    flys = []
    for i in range(N):
        tmp = list(map(int,input().split()))
        flys.append(tmp)
 
 
    final = []
 
    power = power-1
 
    for i in range(0, N):
        for j in range(0, N):
 
            tmp1, tmp2 = shot(i,j,power)
            final.append(tmp1)
            final.append(tmp2)
 
    result = 0
 
    for i in final:
        if i > result:
            result = i
 
    print(f'#{tc} {result}')
