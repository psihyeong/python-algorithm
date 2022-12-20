# BOJ 13144번 List of Unique Numbers

# DP를 활용한 풀이
import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
cnt = [0] * 100001      # 수열을 확인하기 위한 DP
end = 0                 # 투포인터 변수
res = 0
seq_leng = 0            # 수열의 길이

# 투포인터 start
for start in range(N):
    # end값을 증가시키면서 연속된 수열 만들기
    # 중복된 숫자가 나올때까지 수열 생성
    while end < N and not cnt[arr[end]]:
        cnt[arr[end]] += 1
        seq_leng += 1
        end += 1

    # 중복된 수가 나오면 현재까지 연속된 수열의 길이를 더하기
    res += seq_leng

    # 맨 앞쪽 수를 수열에서 제거하고
    cnt[arr[start]] -= 1
    # 수열의 길이 -1
    seq_leng -= 1

print(res)

# deque를 활용한 시간초과 코드
# not in 에서 시간을 크게 잡아먹는듯
# import sys, collections
#
# N = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))
#
# end = 0
# res = 0
# seq = collections.deque()
# for start in range(N):
#
#     while end < N and arr[end] not in seq:
#         seq.append(arr[end])
#         end += 1
#
#     res += len(seq)
#     seq.popleft()
#
# print(res)