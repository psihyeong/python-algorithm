# BOJ 14501번 퇴사
# 브루트포스

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
