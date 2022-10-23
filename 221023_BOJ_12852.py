# BOJ 12852번 1로 만들기 2
# 다이나믹 프로그래밍

N = int(input())
# 인덱스 번호까지 연산하는 횟수의 최솟값과, 그 경로 리스트
dp = [[0,''] for _ in range(N+1)]
dp[1][1] += '1'
for i in range(2,N+1):
    # 1을 빼는 경우
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + ' ' + str(i)

    if i%2 == 0:
        # 2로 나누는 경우가 더 최솟값이면
        if dp[i][0] > dp[i//2][0] + 1:
            # 최솟값 갱신
            dp[i][0] = dp[i//2][0] + 1
            # 경로 갱신
            dp[i][1] = dp[i//2][1] + ' ' + str(i)

    if i%3 == 0:
        # 3으로 나누는 경우가 더 최솟값이면
        if dp[i][0] > dp[i//3][0] + 1:
            # 최솟값 갱신
            dp[i][0] = dp[i//3][0] + 1
            # 경로 갱신
            dp[i][1] = dp[i//3][1] + ' ' + str(i)

print(dp[-1][0])
result = list((dp[-1][1]).split(' '))
print(*result[::-1])
