# BOJ 15650번 N과 M (3)

n, m = list(map(int, input().split()))
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(start)
        s.pop()

dfs(1)
