# SWEA 13994번 새로운 버스 노선

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nosun = []
    for i in range(N):
        tmp = list(map(int,input().split()))
        nosun.append(tmp)
    stop = [0 for i in range(1001)]

    for i in range(0,len(nosun)):

        if nosun[i][0] == 1:

            for j in range(nosun[i][1],nosun[i][2]+1):
                stop[j] += 1

        elif nosun[i][0] == 2:
            for j in range(nosun[i][1],nosun[i][2],2):
                stop[j] += 1

            stop[nosun[i][2]] += 1
        else:
            if nosun[i][1] % 2 == 0:
                for j in range(nosun[i][1],nosun[i][2]):
                    if j%4 == 0:
                        stop[j] += 1
            else:
                for j in range(nosun[i][1],nosun[i][2]):
                    if j%3 == 0:
                        if j%10 != 0:
                            stop[j] += 1

            stop[nosun[i][2]] += 1

    result = 0
    for i in stop:
        if i > result:
            result = i

    print(f'#{tc} {result}')
