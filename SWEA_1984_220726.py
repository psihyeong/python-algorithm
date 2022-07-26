# SWEA 1984. 중간 평균값 구하기

T = int(input())
for tc in range(1,T+1):
    num_list = input()
    num_list = num_list.rstrip(' ') # 공백으로 split을 위해 입력값 끝에 공백 삭제
    num_list = list(map(int,num_list.split()))
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
    result = format(sum(num_list)/len(num_list),"0.0f")
    print(f'#{tc} {result}')
