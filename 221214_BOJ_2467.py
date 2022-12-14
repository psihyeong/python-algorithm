# BOJ 2467번 용액
# 이분탐색, 투 포인터

import sys

N = int(sys.stdin.readline())       # 전체 용액의 수 N
fluids = list(map(int,sys.stdin.readline().split()))    # 용액의 특성값을 담는 리스트

first_res, second_res = 0,0 # 결과 용액 인덱스
now_sum = sys.maxsize       # 초기값
l, r = 0, N-1               # 이분탐색 시작점

while l < r:
    twosum = fluids[l] + fluids[r]      # 두 용액의 합

    # 절댓값이 보다 0에 가까울 경우.
    if abs(twosum) < now_sum:
        # 최신화
        first_res = l
        second_res = r
        now_sum = abs(twosum)

    # 보다 0에 가까운 경우를 찾기 위해
    # 양수면
    if twosum > 0:
        # 양수를 줄여줌
        r -= 1
    # 음수면
    elif twosum < 0:
        # 음수를 줄여줌
        l += 1
    # 0 이면 종료
    else:
        break

print(fluids[first_res], fluids[second_res])