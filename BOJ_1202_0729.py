# 1202번 보석 도둑
import heapq,sys
input=sys.stdin.readline
N, K = map(int,input().split())
stone = []
bag = []
for i in range(N):
  a= list(map(int,input().split()))
  heapq.heappush(stone,a)
for i in range(K):
  a= int(input())
  heapq.heappush(bag,a)

result = 0
temp =[]
while bag:
  cur_bag = heapq.heappop(bag)

  while stone and cur_bag >= stone[0][0]:
    cur_stone = heapq.heappop(stone)
    heapq.heappush(temp,-cur_stone[1])

  if temp:
    result += -heapq.heappop(temp)


print(result)
