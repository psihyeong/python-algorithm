# BOJ 2477번 참외밭

N = int(input())
farm = [list(map(int,input().split())) for _ in range(6)]
w, h = 0, 0
maxhi, maxwi = 0 ,0
for i in range(6):
    if farm[i][0] == 4 or farm[i][0] == 3:
        if farm[i][1] > h:
            h = farm[i][1]
            maxhi = i
    if farm[i][0] == 2 or farm[i][0] == 1:
        if farm[i][1] > w:
            w = farm[i][1]
            maxwi = i
result = 0
result += w*h
result -= (h-min(farm[(maxwi+1)%6][1],farm[maxwi-1][1]))*(w-min(farm[(maxhi+1)%6][1],farm[maxhi-1][1]))
print(result*N)
