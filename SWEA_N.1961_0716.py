T = int(input())
for tc in range(1,T+1):
  n=int(input())
  lst = [input().split() for _ in range(n)]
  lst_90 = []
  for j in range(n):
    tmp = []
    for i in range(n):
      tmp.append(lst[i][j])

    tmp.reverse()
    lst_90.append(tmp)

  lst_180 = []
  for j in range(n):
   tmp = []
   for i in range(n):
      tmp.append(lst_90[i][j])

   tmp.reverse()
   lst_180.append(tmp)

  lst_270 = []
  for j in range(n):
    tmp = []
    for i in range(n):
      tmp.append(lst_180[i][j])

    tmp.reverse()
    lst_270.append(tmp)
  print("#{}".format(tc))
  for i in range(n):
    print(''.join(lst_90[i]),''.join(lst_180[i]),''.join(lst_270[i]))