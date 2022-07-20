#1931 회의실배정
n=int(input())
l=[]
for i in range(n):
  a,b=map(int,input().split(' '))
  l.append([a,b])
  
l.sort(key=lambda x : x[0])
l.sort(key=lambda x : x[1])

result = 1
end = l[0][1]
for i in range(1,n):
  if l[i][0] >= end:
    result+=1
    end = l[i][1]
print(result)
