# BOJ 14501번 퇴사
# 브루트포스, 다이나믹 프로그래밍

# 브루트포스 풀이
def dfs(startwith,val):
    global result
    if result < val:
        result = val
    for i in range(startwith,N+1):
        new_val = val + schedule[i][1]
        new_start = i + schedule[i][0]
        if new_start <= N+1:
            dfs(new_start, new_val)

N = int(input())
schedule = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
result = 0
dfs(1,0)
print(result)


# DP 풀이
N = int(input())
schedule =[[0,0]] + [list(map(int,input().split())) for _ in range(N)]
# 인덱스 날짜에 상담이 끝나고 받는 최대 금액
dp = [0 for _ in range(21)]
for i in range(1,N+1):
    length = schedule[i][0] - 1
    dp[i] = max(dp[i-1],dp[i])
    dp[i+length] = max(dp[i-1] + schedule[i][1], dp[i+length])
print(dp[N])