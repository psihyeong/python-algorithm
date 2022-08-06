#SWEA 1289번 원재의 메모리 복구하기

T = int(input())
for tc in range(1,T+1): 
    check = str(input())
    # input의 첫번째 값이 1이면 전부 1로 한 번은 바꿨다는 말이니 cnt 1부터 출발
    if check[0] == '1':
        cnt = 1
    else:
        cnt = 0
    # 현재값이 다음값과 다를때 마다 cnt+=1
    for i in range(len(check)-1):
        if check[i] != check[i+1]:
            cnt += 1
    print(f'#{tc} {cnt}')
