# 1259번 팰린드롬수
while True:
    check = 1
    n_list = list(map(int,input()))
    if n_list[0] == 0:
        break
    for i in range((len(n_list)//2)):
        if n_list[i] != n_list[-(i+1)]:
            check = 0
            break
    if check == 1:
        print('yes')
    else:
        print('no')
