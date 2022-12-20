# BOJ 13144번 List of Unique Numbers

import sys, collections

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
cnt = [0] * 100001
seq = collections.deque()
end = 0
res = 0


for start in range(N):
    while end < N and not cnt[arr[end]]:
        cnt[arr[end]] += 1
        seq.append(arr[end])
        end += 1
        
    res += len(seq)
    seq.popleft()
    cnt[arr[start]] -= 1

print(res)