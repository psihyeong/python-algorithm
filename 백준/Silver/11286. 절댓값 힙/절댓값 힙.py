# BOJ 11286번 절댓값 힙
import sys
import heapq
input=sys.stdin.readline


N = int(input())
nums = []
for _ in range(N):
    tmp = int(input())

    
    if tmp == 0:
        if len(nums) == 0:
            print(0)
        else:
            print(heapq.heappop(nums)[1])
    else:
        heapq.heappush(nums,(abs(tmp),tmp))