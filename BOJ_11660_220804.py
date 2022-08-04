#BOJ 11660번 구간 합 구하기 5
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
for i in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)

# 1,1 부터 index 번호까지의 구간 합
# 좌표와 index를 맞춰주기 위해 index값 0에 0을 깔아둠
sum_list = [[0 for i in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
       # 구간 합을 구하는 점화식
       sum_list[i][j] = sum_list[i-1][j]+sum_list[i][j-1]-sum_list[i-1][j-1]+graph[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_list[x2][y2] + sum_list[x1-1][y1-1] - sum_list[x1-1][y2] - sum_list[x2][y1-1]
    print(result)
