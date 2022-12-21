# BOJ 22862번 가장 긴 짝수 연속한 부분 수열 (large)

import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

res = 0     # 결과값
end = 0     # 투포인터 변수
even, odd = 0, 0    # 짝수, 홀수의 개수

# 투포인터 시작
for start in range(N):
    # 홀수 삭제 가능한 만큼 end 포인터 옮기기
    while end < N and K >= odd:
        if arr[end] % 2:
            odd += 1
        else:
            even += 1
        end += 1

    # 결과값 갱신
    res = max(res, even)

    # start포인터 옮기기
    if arr[start] % 2:
        odd -= 1
    else:
        even -= 1

print(res)
