# SWEA 2005. 파스칼의 삼각형

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    if N == 1:
        pascal = [[1]]
    else:
        check = 2
        pascal = [[1],[1,1]]
        while check != N:
            temp = []
            temp.append(1)
            for i in range(len(pascal[-1])-1):
                temp.append(pascal[-1][i]+pascal[-1][i+1])
            temp.append(1)
            pascal.append(temp)
            check += 1

    print(f'#{tc}')
    for row in pascal:
        for i in row:
            print(i,end=' ')
        print() 
