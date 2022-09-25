# BOJ 15652번 N과 M (4)

n, m = list(map(int, input().split()))
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n + 1):
        if len(s) == 0:
            s.append(i)
            dfs(start)
            s.pop()

        else:
            if s[-1] <= i:
                s.append(i)
                dfs(start)
                s.pop()

dfs(1)
