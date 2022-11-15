# BOJ 1699번 제곱수의 합
# 다이나믹 프로그래밍

N = int(input())

# 인덱스 번호를 제곱수의 합으로 나타날 때 제곱수 항의 최소 개수
# 초기값: 1의 제곱으로만 이루어진 인덱스 제곱수의 합
dp = [i for i in range(N+1)]

# 보텀업 DP
for i in range(1,N+1):
    # 2 이상의 제곱수의 경우
    for j in range(2,i):
        r = j**2
        # 해당 제곱수가 들어갈 수 있는 i 이면
        if r > i:
            break
        # 최솟값 갱신
        if dp[i] > dp[i - r] + 1:
            dp[i] = dp[i - r] + 1

print(dp[N])

