# SWEA 1244번 최대 상금

def dfs(count):
    global result
    if not count:
        tmp = int(''.join(values))
        if result < tmp:
            result = tmp
        return
    for i in range(length):
        for j in range(i + 1, length):
            values[i], values[j] = values[j], values[i]
            tmp_key = ''.join(values)
            if visited.get((tmp_key, count - 1), 1):
                visited[(tmp_key, count - 1)] = 0
                dfs(count - 1)
            values[i], values[j] = values[j], values[i]
 
TC = int(input())
for tc in range(1,TC+1):
    result = -1
    value, change = input().split()
    values = list(value)
    change = int(change)
    length = len(values)
    visited = {}
    dfs(change)
    print(f'#{tc} {result}')
