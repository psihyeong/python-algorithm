# SWEA 2115번 벌꿀채취

# 벌꿀 리스트 중 최대수익을 갱신하는 함수
def cal(lst,beginwith):
    global result
    # 최대양보다 적은 조합이면
    if sum(tmp) <= C:
        tmp_val = 0
        for i in tmp:
            tmp_val += (i**2)
        # 최대 수익 갱신
        if tmp_val > result:
            result = tmp_val
    # 최대 M개의 조합을 구하는 반복문
    for i in range(beginwith,M):
        tmp.append(lst[i])
        cal(lst,i+1)
        tmp.pop()

for tc in range(1,int(input())+1):
    N, M, C = map(int,input().split())
    honeys = [list(map(int,input().split())) for _ in range(N)]
    # 인덱스 위치부터 M개의 꿀을 채취했을 때 최대수익 받는 리스트
    dp = [[0 for _ in range(N-M+1)] for _ in range(N)]
    # 1번째 줄부터
    for row in range(N):
        # 가능한 가로의 경우의 수만큼
        for i in range(N-M+1):
            result = 0
            tmp = []
            # 최대 수익을 구해서
            cal(honeys[row][i:i+M],0)
            # 갱신
            dp[row][i] = result

    res = 0
    # 두 일꾼이 한 줄에서 채집이 가능한 경우
    if M*2 >= N:
        for row in range(N):
            # 첫번째 일꾼 인덱스가 i면
            for i in range(N-M+1-M):
                # 두번째 일꾼이 가능한 인덱스는 j
                for j in range(i+M,N-M+1):
                    tmp = dp[row][i] + dp[row][j]
                    res = max(res,tmp)

    # 두 일꾼이 서로 다른 줄에서 채집할 경우
    tmp = []
    for row in range(N):
        tmp.append(max(dp[row]))
    tmp.sort(reverse=True)
    res = max(res,tmp[0]+tmp[1])
    print(f'#{tc} {res}')