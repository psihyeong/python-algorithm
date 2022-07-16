T = int(input())
for test_case in range(1, T+1):
  a,b = map(int,input().split())
  listA=list(map(int,input().split()))
  listB=list(map(int,input().split()))
  if a > b:
    a, b= b, a
    listA, listB = listB, listA
  max = 0
  for i in range(b-a+1):
    ans=0
    for j in range(a):
      ans+=listA[j]*listB[j+i]
    if ans > max:
      max = ans
  print("#{} {}".format(test_case,max))