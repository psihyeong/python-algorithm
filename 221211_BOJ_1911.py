# BOJ 1911번 흙길 보수하기

import sys

N, L = map(int,sys.stdin.readline().split())
ponds = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ponds.sort(key=lambda x:x[0])       # 물웅덩이 위치 오름차순 정렬

cnt_pan = 0     # 널빤지의 가장 오른쪽 끝 지점
end_pan = 0     # 널빤지 개수
for start, end in ponds:
    # 널빤지를 잇지 못하고 새로 까는 경우
    if end_pan < start:
        end_pan = start     # 위치 최신화

    # 널빤지 깔기
    while end_pan < end:
        cnt_pan += 1
        end_pan += L

print(cnt_pan)