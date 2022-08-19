# BOJ 17406번 배열 돌리기 4
from itertools import permutations
import copy

def rotate(r,c,s):
    # 모서리들 좌표
    left_top = (r-s-1,c-s-1)
    right_top = (r-s-1, c+s-1)
    left_bottom = (r+s-1,c-s-1)
    right_bottom = (r+s-1,c+s-1)

    # 모서리 값 따로 저장
    edge_tmp = [
        arr[left_top[0]][left_top[1]],
        arr[left_bottom[0]][left_bottom[1]],
        arr[right_bottom[0]][right_bottom[1]],
        arr[right_top[0]][right_top[1]]
    ]

    # 윗줄 오른쪽으로 밀기
    for i in range(right_top[1], left_top[1],-1):
        arr[left_top[0]][i] = arr[left_top[0]][i-1]
    # 오른쪽 줄 아래로 밀기
    for i in range(right_bottom[0],right_top[0],-1):
        arr[i][right_top[1]] = arr[i-1][right_top[1]]
    # 아랫줄 왼쪽으로 밀기
    for i in range(left_bottom[1], right_bottom[1]):
        arr[left_bottom[0]][i] = arr[left_bottom[0]][i+1]
    # 왼쪽 줄 위로 밀기
    for i in range(left_top[0], left_bottom[0]):
        arr[i][left_top[1]] = arr[i+1][left_top[1]]

    # 모서리 값 제자리 찾아가기
    arr[left_top[0]][left_top[1]+1] = edge_tmp[0]
    arr[left_bottom[0]-1][left_bottom[1]] = edge_tmp[1]
    arr[right_bottom[0]][right_bottom[1]-1] = edge_tmp[2]
    arr[right_top[0]+1][right_top[1]] = edge_tmp[3]

N, M, R = map(int,input().split())

original_arr = [list(map(int,input().split())) for _ in range(N)]

command = [list(map(int,input().split())) for _ in range(R)]

result = 99999999

all_per = list(permutations(command,len(command)))
# 모든 회전연산 순서의 경우의 수
for n in all_per:
    # 경우의 수 시작 전에 최초 배열 초기화
    arr = copy.deepcopy(original_arr)
    # 회전 연산
    for com in n:
        # 테두리별 돌리기
        for i in range(com[2],0,-1):
            rotate(com[0],com[1],i)
    # 해당 경우의 수가 끝났을 때 최솟값 갱신
    for row in arr:
        if sum(row) < result:
            result = sum(row)

print(result)
