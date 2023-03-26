from itertools import combinations_with_replacement


def solution(n, apeech):
    answer = [-1]
    max_gap = 0

    for comb in combinations_with_replacement(range(11), n):  # 중복 조합으로 0~10점까지 n개 뽑기
        apeech_point, lion_point = 0, 0
        lion = [0] * 11         # 라이언의 과녁 정보
        for i in comb: 
            lion[10 - i] += 1
            
        for i in range(11):
            if lion[i] > apeech[i]:     # 라이언이 점수를 획득하는 경우
                lion_point += 10 - i
            elif apeech[i] != 0:        # 어피치가 점수를 획득하는 경우
                apeech_point += 10 -i
        
        if lion_point > apeech_point:   # 라이언이 우승할 경우
            gap = lion_point - apeech_point
            if gap > max_gap:           # 최댓값 갱신
                max_gap = gap
                answer = lion
                
    return answer

'''
순조부 실패 코드

def solution(n, info):
    answer = []
    
    stat = [0 for _ in range(11)]
    
    def cal_result(stat,info):
        my_p = 0
        rival_p = 0
        for i in range(11):
            if stat[i] > info[10-i]:
                my_p += i
            else:
                rival_p += i
        
        if my_p > rival_p:
            return (1, my_p-rival_p)
        else:
            return (0, my_p-rival_p)
                
    max_point = 0
        
    def dfs(res_point, left_arrow, target):
        nonlocal max_point, answer
        if target == -1 or left_arrow == 0:
            is_win, p = cal_result(stat,info)
            if is_win:
                if p > max_point:
                    max_point = p
                    answer = stat[::]
                    print(p,answer)
            return
        else:
            for i in range(left_arrow):
                stat[target] = i
                if i > info[target]:
                    total_point = res_point+target
                    dfs(total_point, left_arrow-i, target-1)
                else:
                    dfs(res_point, left_arrow-i, target-1)
                stat[target] = 0                
    
    dfs(0,n,10)
    
    return answer
'''
