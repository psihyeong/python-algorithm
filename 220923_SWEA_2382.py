# SWEA 2382번 미생물 격리

TC = int(input())
for tc in range(1,TC+1):
    N, M ,K = map(int,input().split())
    misaeng = [list(map(int,input().split())) for _ in range(K)]
    d = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
    for _ in range(M):
        # 크기가 큰 미생물 부터 보기
        misaeng.sort(key=lambda x : x[2],reverse=True)
        for i in range(len(misaeng)):
            # 크기가 0이상 == 살아있는 미생물일때,
            if misaeng[i][2] > 0:
                y = misaeng[i][0]
                x = misaeng[i][1]
                size = misaeng[i][2]
                di = misaeng[i][3]
                ny = y + d[di][0]
                nx = x + d[di][1]
                # 첫번째 미생물은 바로 위치 갱신
                if i == 0:
                    # 이동
                    misaeng[i][0] = ny
                    misaeng[i][1] = nx
                    # 가장자리일 때 크기와, 방향 갱신
                    if ny == 0 and di == 1:
                        misaeng[i][3] = 2
                        misaeng[i][2] = size // 2
                    elif ny == N - 1 and di == 2:
                        misaeng[i][3] = 1
                        misaeng[i][2] = size // 2
                    elif nx == 0 and di == 3:
                        misaeng[i][3] = 4
                        misaeng[i][2] = size // 2
                    elif nx == N - 1 and di == 4:
                        misaeng[i][3] = 3
                        misaeng[i][2] = size // 2
                # 두번째 미생물부터
                else:
                    # 앞에 미생물들과 비교해서
                    for j in range(0,i):
                        # 이미 자리잡은 더 큰 미생물이 있는 경우,
                        if ny == misaeng[j][0] and nx == misaeng[j][1]:
                            # 잡아먹히고
                            misaeng[j][2] += size
                            # 소멸
                            misaeng[i][0] = 0
                            misaeng[i][1] = 0
                            misaeng[i][2] = 0
                            misaeng[i][3] = 0
                            break
                        # 자리잡은 미생물이 없으면
                        else:
                            # 이동
                            misaeng[i][0] = ny
                            misaeng[i][1] = nx
                            # 가장자리일 때 크기와 방향 갱신,
                            if ny == 0 and di == 1:
                                misaeng[i][3] = 2
                                misaeng[i][2] = size//2
                            elif ny == N-1 and di == 2:
                                misaeng[i][3] = 1
                                misaeng[i][2] = size//2
                            elif nx == 0 and di == 3:
                                misaeng[i][3] = 4
                                misaeng[i][2] = size//2
                            elif nx == N-1 and di == 4:
                                misaeng[i][3] = 3
                                misaeng[i][2] = size//2

    result = 0
    for i in misaeng:
        result += i[2]
    print(f'#{tc} {result}')
