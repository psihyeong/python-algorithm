# BOJ 5567번 결혼식

n = int(input())
m = int(input())
fr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    fr[a].append(b)
    fr[b].append(a)

# 상근이와 몇 다리 건넌 친구인지
visited = [0 for _ in range(n+1)]
visited[1] = 1
stack = [1]

while stack:
    a = stack.pop()
    # 친구이면서
    for f in fr[a]:
        # 친구가 된 적 없다면
        if not visited[f]:
            # 몇 다리 인지 갱신
            visited[f] = visited[a] + 1
            stack.append(f)
        # 이미 친구가 맺어졌는데
        else:
            # 더 짧은 다리로 친구가 된 경우가 있다 갱신
            if visited[f] > visited[a] + 1:
                visited[f] = visited[a] + 1
res = 0
for i in visited:
    # 1다리 또는 2다리 친구인 경우
    if 1 <= i-1 <= 2:
        res += 1

print(res)
