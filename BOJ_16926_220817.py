# BOJ 16926번 배열돌리기1

import sys
input = sys.stdin.readline

def rotate(edge):
    # 모서리들 좌표
    left_top = (edge,edge)
    right_top = (edge, M - edge - 1)
    left_bottom = (N - edge - 1,edge)
    right_bottom = (N - edge - 1,M - edge - 1)

    # 모서리 값 따로 저장
    edge_tmp = [
        arr[left_top[0]][left_top[1]],
        arr[left_bottom[0]][left_bottom[1]],
        arr[right_bottom[0]][right_bottom[1]],
        arr[right_top[0]][right_top[1]]
        ]

    # 윗줄 왼쪽으로 밀기
    for i in range(left_top[1], right_top[1]):
        arr[left_top[0]][i] = arr[left_top[0]][i + 1]
    # 왼쪽 줄 아래로 밀기
    for i in range(left_bottom[0], left_top[0], -1):
        arr[i][left_top[1]] = arr[i - 1][left_top[1]]
    # 아랫줄 오른쪽으로 밀기
    for i in range(right_bottom[1], left_bottom[1], -1):
        arr[left_bottom[0]][i] = arr[left_bottom[0]][i - 1]
    # 오른쪽 줄 위로 밀기
    for i in range(right_top[0], right_bottom[0]):
        arr[i][right_top[1]] = arr[i+1][right_top[1]]
    # 모서리 값 제자리 찾아가기
    arr[left_top[0] + 1][left_top[1]] = edge_tmp[0]
    arr[left_bottom[0]][left_bottom[1] + 1] = edge_tmp[1]
    arr[right_bottom[0]-1][right_bottom[1]] = edge_tmp[2]
    arr[right_top[0]][right_top[1]-1] = edge_tmp[3]

N, M, R = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
border_n = 0
# 테두리 개수 구하기
if N > M:
    border_n = M//2
else:
    border_n = N//2

for _ in range(R):
    # 테두리별 돌리기
    for i in range(border_n):
        rotate(i)

for row in arr:
    for i in row:
        print(i,end=' ')
    print()
