N= int(input())
def sugar(n) :
    list= []
    for i in range(0, n//5+1):
        f = 5*i
        for j in range(0,n//3+1):
          t = 3*j
          if f+t==n:
            list.append(i+j)
    if len(list) == 0:
      return -1
    else:
      return min(list)

print(sugar(N))
