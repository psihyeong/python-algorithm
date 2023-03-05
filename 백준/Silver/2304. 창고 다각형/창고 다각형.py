import sys
from collections import deque

N = int(sys.stdin.readline())       # 기둥의 개수
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x:x[0])    # 위치를 기준으로 내림차순 정렬한 (기둥의 위치, 기둥의 높이) 튜플 리스트


mh = 0      # 가장 높은 기둥의 높이
mh_idx = 0  # 가장 높은 기둥의 인덱스 번호
for i in range(N):
    high = arr[i][1]
    if high > mh:
        mh = high
        mh_idx = i

left_que = deque(arr[:mh_idx + 1])      # 가장 높은 기둥 기준 왼쪽 기둥들의 정보를 담는 큐
right_stack = arr[mh_idx:]              # 가장 높은 기둥 기준 오른쪽 기둥들의 정보를 담는 스택

res = mh        # 결과값, 초기값 = 가장 높은 기둥의 높이

# 왼쪽 창고의 넓이 구하기
nl, nh = 0, 0
while left_que:
    loc, high = left_que.popleft()
    if high >= nh:
        res += (loc - nl) * nh
        nl = loc
        nh = high

# 오른쪽 창고의 넓이 구하기
nl, nh = 0, 0
while right_stack:
    loc, high = right_stack.pop()
    if high >= nh:
        res += (nl-loc) * nh
        nl = loc
        nh = high

print(res)