# BOJ 2164번 카드2

from collections import deque

N = int(input())
deq = deque()
for i in range(1, N+1):
    deq.append(i)
for _ in range(N-2):
    deq.popleft()
    temp = deq.popleft()
    deq.append(temp)

if N == 1:
    print(1)
else:
    print(deq[1])
