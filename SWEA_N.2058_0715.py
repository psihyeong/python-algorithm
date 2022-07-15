''' SWEA 2058번 자릿수 더하기'''

number=int(input())
result=0

while True:
  if number == 0:
    break
  result+=number%10
  number//=10

print(result)  