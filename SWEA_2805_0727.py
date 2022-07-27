# SWEA 2805. 농작물 수확하기

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        temp = list(map(str,input()))
        farm.append(temp)
    # 농장 문자열 2차원 리스트 
    revenue = 0
    for i in farm[N//2]:
        revenue += int(i)
    # 농장의 가운데 행 모두 수익에 더하기
    mid = N//2
    for i in range(1,mid+1):
        for j in farm[mid-i][i:N-i]:
            revenue += int(j)
        # 가운데에서 윗행들의 수익
        for k in farm[mid+i][i:N-i]:
            revenue += int(k)
        # 가운데에서 아래행들의 수익
    print(f'#{tc} {revenue}')
