# 4796번 캠핑
lst = []

while True:
  a = list(map(int,input().split()))
  lst.append(a)
  if a == [0,0,0]:
    break

for i in range(len(lst)-1):
  if lst[i][2]%lst[i][1] > lst[i][0]:
    result = lst[i][2]//lst[i][1]*lst[i][0] + lst[i][0]
  else:
    result = lst[i][2]//lst[i][1]*lst[i][0] + lst[i][2]%lst[i][1]
  print("Case {}: {}".format(i+1,result))
