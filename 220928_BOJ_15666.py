# BOJ N과 M (12)

def DFS(depth):
    if depth == M:
        print(*tmp)
        return
    else:
        # 같은 수를 여러 번 골라도 됨
        for i in num_lst:
            # 비내림차순 조건
            if depth == 0 or tmp[-1] <= i:
                tmp.append(i)
                DFS(depth+1)
                tmp.pop()

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
# 중복 제거
num_lst = sorted(list(set(numbers)))
tmp = []
DFS(0)
