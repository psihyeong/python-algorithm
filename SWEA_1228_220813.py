# SWEA 1228번 암호문1

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    # 원본 암호문
    origin = list(map(int,input().split()))
    com_n = int(input())
    com = list(map(str,input().split('I ')))
    # 명령어 리스트
    command = []
    for i in range(1,com_n+1):
        command.append(list(com[i].split()))
    # 첫번째 명령문 부터 수행
    for i in command:
        for j in range(len(i)-1,1,-1):
            origin.insert(int(i[0]),int(i[j]))
    
    print(f'#{tc}',end=' ')
    for n in range(10):
        print(origin[n],end=' ')
    print()
