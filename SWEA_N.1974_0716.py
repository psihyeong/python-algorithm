T = int(input())
for tc in range(1,T+1):
  lst = [input().split() for _ in range(9)]
  result = 1
  for i in range(9):
    check = set()
    for j in range(9):
      check.add(lst[i][j])
    if len(check) != 9:
      result = 0
      break

  for i in range(9):
    check = set()
    for j in range(9):
      check.add(lst[j][i])
    if len(check) != 9:
      result = 0
      break

  for i in range(0,9,3):
    for j in range(0,9,3):
      check = set()
      for k in range(3):
        for t in range(3):
          check.add(lst[i+k][j+t])
      if len(check) != 9:
        result = 0
        break     
  print("#{} {}".format(tc,result))