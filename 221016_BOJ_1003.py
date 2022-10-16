# BOJ 1003번 피보나치 함수
# 다이나믹 프로그래밍

for tc in range(int(input())):
    N = int(input())
    # N번째 피보나치 수를 구할 때 호출되는 0과 1의 수
    dp = [[0,0] for _ in range(N+1)]
    if N >= 0:
        dp[0][0] = 1
    # 인덱스 에러를 막기 위해 N이 0이면 적용되지 않는 조건
    if N >= 1:
        dp[1][1] = 1
    # 인덱스 에러를 막기 위해 N이 0이거나 1이면 적용되지 않는 조건
    if N >= 2:
        for i in range(2,N+1):
            # 점화식
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(*dp[N])

# 시간초과 코드
# def fibo(n):
#     global zero, one
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# for tc in range(int(input())):
#     N = int(input())
#     zero, one = 0,0
#     result = fibo(N)
#     print(zero, one)
