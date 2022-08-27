# BOJ 1244번 스위치 켜고 끄기

N = int(input())
onoff = list(map(int,input().split()))
student_N = int(input())
switch = [list(map(int,input().split())) for _ in range(student_N)]
start, end = 0,0
for s in switch:
    if s[0] == 1:
        mi = s[1]-1

        while mi < N:
            onoff[mi] = (onoff[mi]+1) % 2
            mi += s[1]

    elif s[0] == 2:
        wi = s[1]-1
        cnt = 0
        while wi-cnt >= 0 and wi+cnt < N:
            if onoff[wi-cnt] == onoff[wi+cnt]:
                start = wi-cnt
                end = wi+cnt
                cnt += 1
            else:
                break

        for idx in range(start, end+1):
            onoff[idx] = (onoff[idx]+1) % 2


for i in range(1,N+1):
    print(onoff[i-1], end=' ')
    if i%20 == 0:
        print()
