#1018 체스판 다시 칠하기
N, M = map(int, input().split())

my_chess = []
for _ in range(N):
    my_chess.append(input())

check_pan1 = []
check_pan2 = []
case = []
line = ''
for i in range(8):    
    if i % 2 == 0:
        line += 'W'
    else:
        line += 'B'
re_line = line[::-1]

for i in range(8):
    if i % 2 == 0:
        check_pan1.append(line)
        check_pan2.append(re_line)
    else:
        check_pan1.append(re_line)
        check_pan2.append(line)

for k in range(M-7):
    for h in range(N-7):
        temp1 = 0
        for i in range(8):
            for j in range(8):
                if check_pan1[i][j] != my_chess[i+h][j+k]:
                    temp1 += 1
        case.append(temp1)

for k in range(M-7):
    for h in range(N-7):
        temp2 = 0
        for i in range(8):
            for j in range(8):
                if check_pan2[i][j] != my_chess[i+h][j+k]:
                    temp2 += 1
        case.append(temp2)
            
print(min(case))
