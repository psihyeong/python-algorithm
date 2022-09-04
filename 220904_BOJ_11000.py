# BOJ 11000번 강의실 배정

import heapq, sys

input=sys.stdin.readline
n=int(input())
time=[]
for i in range(n):
  x,y = map(int,input().split())
  time.append([x,y])
      
time.sort()

room=[]
heapq.heappush(room, time[0][1])
      
for i in range(1,n):
  if room[0] > time[i][0]: #회의실 하나 더 만들어야함.
    heapq.heappush(room, time[i][1])#하나 더 만들어서 회의끝나는 시간 최신화
  else:
    heapq.heappop(room)#하나 더 만들지 않고 기존시간 빼고 새로운 시간 넣으면서 시간 최신화
    heapq.heappush(room,time[i][1])

print(len(room))
